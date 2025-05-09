# Simple Chatbot 🤖

A basic Python chatbot that learns how to respond to user input by saving custom replies during conversation. Perfect for beginners learning Python, input handling, dictionaries, and randomization.

---

## 💡 Features

- Learns responses from the user in real time
- Supports multiple possible replies for the same input
- Randomly chooses a response when multiple are available
- Can clear the screen with `clean` and exit with `bye`

---

## 📦 Requirements

- Python 3.x

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/AlirezaAhmadiTech/Simple-chatbot.git

---

📝 Notes
You can teach the bot new responses during the conversation.

To provide multiple responses for the same input, separate them with a hyphen -.
For example: hi-hello-hey

The bot will randomly choose one reply each time you use that input.

All learned responses are saved in a file named responses.json

🧠 Your responses will be saved even after you close the program

Type clean to clear the screen, and bye to exit the chatbot.

Bonus: Now the bot has a split personality — you never know what it’ll say 😄


## 🛠️ Example Conversation

```text
You: hello
Bot: I don't know how to respond to that.
Teach me how to reply: hi-hello-hey
Bot: Got it! I'll remember that.

You: hello
Bot: hey

You: clean
# (screen clears)

You: bye
Bot: Goodbye!

