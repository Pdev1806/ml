import requests

def ask_ai(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model" : "mistral",
        "prompt" : prompt,
        "stream" : False,
        "num_predict" : 80
    }
    r = requests.post(url, json=data)
    return r.json()["response"]

def parse(cmd):
    words = cmd.split()
    if len(words)>0 and words[0]=="explain":
        topic = " ".join(words[1:])
        return("explain", topic)
    elif "quiz" in words:
        topic = " ".join(words[1:])
        return("quiz", topic)     
    elif "read" in words:
        topic = " ".join(words[1:])
        return("read", topic)
    else:
        return("unknown", None)

def read_file(subject):
    filename = f"notes/{subject}.txt"
    try:
        with open (filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None
    
print("Offline AI assistant(to quit type 'exit')")
while True:
    cmd = input(">> ").lower().strip()
    if cmd == "exit":
        break
    action, data = parse(cmd)
    if action == "explain":
        if not data:
            print("explain what?")
            continue
        prompt = f"Explain {data}"
        answer = ask_ai(prompt)
        print(answer)
    elif action == "quiz":
        topic = data if data else "general"
        if not topic:
            print("quiz on what?")
            continue
        prompt = f"Generate a quiz on {topic}"
        quiz = ask_ai(prompt)
        print(quiz)
    elif action == "read":
        subject = data.strip()
        if not data:
            print("read what?")
            continue
        notes = read_file(subject)
        if not notes:
            print(f"notes not found.")
        else:
            print(notes)
    else:
        print("unknown command")
