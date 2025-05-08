import random
import json
import os

RESPONSES_FILE = "responses.json"

# Load saved responses
if os.path.exists(RESPONSES_FILE):
    with open(RESPONSES_FILE, "r") as f:
        responses = json.load(f)
else:
    responses = {}

print("Welcome to Simple Chatbot! Type 'bye' to exit or 'clean' to clear the screen.")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    elif user_input == "clean":
        os.system("cls" if os.name == "nt" else "clear")
        continue

    elif user_input in responses:
        print("Bot:", random.choice(responses[user_input]))

    else:
        print("Bot: I don't know how to respond to that.")
        new_response = input("Teach me how to reply: ").strip()
        if new_response:
            responses[user_input] = [new_response]
            print("Bot: Got it! I'll remember that.")
        else:
            print("Bot: No response saved.")

# Save responses to file
with open(RESPONSES_FILE, "w") as f:
    json.dump(responses, f, indent=4)
