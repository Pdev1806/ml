def parse(cmd):
    words = cmd.split()

    if len(words)>0 and words[0] == 'explain':
        topic = " ".join(words[1:])
        return("explain", topic )
    if "quiz" in words:
        topic = " ".join(words[1:])
        return('quiz', topic)
    if "read" in words:
        topic = " ".join(words[1:])
        return('read', topic)
    return("unknown", None)

while True:
    cmd = input("> ").lower().strip()
    if cmd == "exit":
        break
    action, data = parse(cmd)
    if action == "explain":
        print("Explining " + data)
    elif action == "quiz":
        print("Quiz on " + data)
    elif action == "read":
        subject = data.strip()
        filename = f"basics/{subject}.txt"
        try:
            with open(filename, "r") as f:
                notes = f.read()
                print(f"notes for {subject}")
                print(notes)
        except FileNotFoundError:
            print(f"Notes for '{subject}' not found.")
    else:
        print("unknown command")