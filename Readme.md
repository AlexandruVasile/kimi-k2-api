# 🧠 KIMI K2 API Wrapper

 Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model with 32 billion activated parameters and 1 trillion total parameters.

This project provides a simple FastAPI-based web server that wraps around the [Kimi.com](https://www.kimi.com/) web interface. It uses Selenium to simulate interaction with the Kimi chatbot via a headless Chrome browser.

You can send prompts to Kimi programmatically through an HTTP API and get responses back, making this useful for automation, research, or integrating Kimi into other applications.

---

## 🚀 How to Run the API

1. **Install Dependencies**

Make sure you have the following installed:

- Python 3.7+
- Google Chrome
- ChromeDriver (must be compatible with your Chrome version)
- Python packages:

```bash
pip install fastapi uvicorn selenium requests
```

2. **Start the FastAPI Server**

From the terminal, run:

```bash
uvicorn kimik2_api:app --reload
```

This will start the API server at `http://127.0.0.1:8000`.

---

## 📡 How to Call the API

You can use the provided script `call_kimik2_api.py` to send prompts to the API.

### Usage:

```bash
python call_kimik2_api.py "your_prompt"
```

You can also specify a custom API URL (default is `http://127.0.0.1:8000/kimi`):

```bash
python call_kimik2_api.py "your_prompt" --url http://your-server:port/kimi
```

---

## 🤩 How It Works

### API Endpoint

- **`GET /kimi?prompt=your_text`**

  Sends a prompt to the Kimi chatbot and returns the response in JSON format:

```json
{
  "prompt": "your_text",
  "response": "Kimi's reply here"
}
```

### Behind the Scenes

The FastAPI backend uses Selenium to:

1. Open the Kimi website.
2. Enter the user's prompt into the chat input.
3. Click the send button.
4. Wait for the response to appear.
5. Extract the final paragraph of the response.

The interaction mimics a human using the web interface, which makes it compatible with services that don’t offer a public API.

---

## ⚠️ Notes and Warnings

- **Performance**: Each API call launches a new Chrome instance, which can be resource-intensive.
- **Stability**: If Kimi changes their website layout or class names, this script may break.
- **Headless Mode**: Chrome runs in headless mode by default, but you can disable this for debugging by modifying the `get_kimik_response()` function.
- **Rate Limits**: Avoid spamming requests too quickly, as it might get your IP rate-limited or blocked.

---

## 🥪 Example Response

```bash
python call_kimik2_api.py "What is the capital of France?"
```

Output:

```json
{
  "prompt": "What is the capital of France?",
  "response": "The capital of France is Paris."
}
```

---

## 📁 File Structure

```
.
├── kimik2_api.py          # FastAPI server and Selenium logic
├── call_kimik2_api.py     # CLI script to call the API
├── README.md              # This file
```

---

## 🛠 Future Improvements

- Logging in. Right now, it is enough to use short prompts for bypassing the login and make the model working
- Reuse browser sessions for better performance
- Add support for streaming responses
- Dockerize the app for easier deployment
