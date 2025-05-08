import os
import random
import json

RESPONSES_FILE = "responses.json"

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def load_responses():
    if os.path.exists(RESPONSES_FILE):
        with open(RESPONSES_FILE, "r") as file:
            return json.load(file)
    return {}

def save_responses(data):
    with open(RESPONSES_FILE, "w") as file:
        json.dump(data, file, indent=4)

def parse_multiple_answers(answers):
    return [answer.strip() for answer in answers.split("-")]

def main():
    responses = load_responses()

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("BOT: Goodbye!")
            break

        elif user_input == "clean":
            clear_terminal()
            continue

        elif user_input not in responses:
            bot_reply = input("BOT: How should I answer that? ")
            if "-" in bot_reply:
                responses[user_input] = parse_multiple_answers(bot_reply)
            else:
                responses[user_input] = bot_reply
            save_responses(responses)

        else:
            reply = responses[user_input]
            if isinstance(reply, list):
                print(f"BOT: {random.choice(reply)}")
            else:
                print(f"BOT: {reply}")

if __name__ == "__main__":
    main()
