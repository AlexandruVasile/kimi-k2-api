from fastapi import FastAPI, Query
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

app = FastAPI()

KIMIK2_URL = "https://www.kimi.com/"
TEXT_EDITOR_CLASS_NAME = "chat-input-editor"
SEND_BUTTON_CLASS_NAME = "send-button"
KIMIK2_ANSWER_CLASS = "markdown"

def get_kimik_response(prompt: str, headless: bool = True) -> str:
    # Configure WebDriver
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(KIMIK2_URL)

        wait = WebDriverWait(driver, 20)
        chat_editor = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, TEXT_EDITOR_CLASS_NAME)))
        chat_editor.click()
        chat_editor.send_keys(prompt)

        send_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, SEND_BUTTON_CLASS_NAME)))
        send_button.click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "stop")))

        while True:
            try:
                driver.find_element(By.CLASS_NAME, "stop")
                time.sleep(0.5)
            except NoSuchElementException:
                break

        paragraphs = driver.find_elements(By.CLASS_NAME, KIMIK2_ANSWER_CLASS)
        if paragraphs:
            return paragraphs[-1].text
        else:
            return "No response found."

    finally:
        driver.quit()

@app.get("/kimi")
def ask_kimi(prompt: str = Query(..., description="Prompt to send to Kimi")):
    try:
        response = get_kimik_response(prompt)
        return {"prompt": prompt, "response": response}
    except Exception as e:
        return {"error": str(e)}
