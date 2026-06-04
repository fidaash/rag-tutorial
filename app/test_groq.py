import requests

GROQ_API_KEY = "gsk_твой_ключ_сюда"

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}
body = {
    "model": "llama3-8b-8192",
    "messages": [{"role": "user", "content": "Say hello"}],
    "max_tokens": 50,
}

resp = requests.post(url, headers=headers, json=body, timeout=15)
print(resp.status_code)
print(resp.json())
