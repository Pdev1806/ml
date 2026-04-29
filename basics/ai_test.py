import requests

url = "http://localhost:11434/api/generate"

x = input("Enter prompt: ")
data = {
    "model" : "mistral",
    "prompt" : x,
    "stream" : False
}

r = requests.post(url, json=data)
print(r.json()["response"])