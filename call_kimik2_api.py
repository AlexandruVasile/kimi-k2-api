import requests
import argparse

def call_kimi_api(prompt, url):
    params = {"prompt": prompt}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Send a prompt to the Kimi API")
    parser.add_argument("prompt", type=str, help="The prompt to send")
    parser.add_argument(
        "--url",
        type=str,
        default="http://127.0.0.1:8000/kimi",
        help="The URL of the Kimi API endpoint (default: http://127.0.0.1:8000/kimi)"
    )
    args = parser.parse_args()

    result = call_kimi_api(args.prompt, args.url)
    print(result)

if __name__ == "__main__":
    main()
