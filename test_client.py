import requests

url = "http://127.0.0.1:8000/analyze"
payload = {
    "text": "Hey, I need help upgrading my subscription plan from Free to Pro."
}

try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("Error connecting to FastAPI server:", e)
