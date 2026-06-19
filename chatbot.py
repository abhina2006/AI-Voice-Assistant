import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

engine = pyttsx3.init()
recognizer= sr.Recognizer()


def save_log(user, bot):
    with open("conversation_log.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}]\n")
        file.write(f"User: {user}\n")
        file.write(f"Bot: {bot}\n\n")

while True:
    print("\n1. Type")
    print("2. Voice")
    choice = input("Choose (1/2): ")

    if choice == "1":
        user = input("You: ").lower()

    elif choice == "2":
        with sr.Microphone() as source:
            print("Speak now...")
            audio = recognizer.listen(source)

        try:
            user = recognizer.recognize_google(audio).lower()
            print("You said:", user)
        except:
            print("Sorry, could not understand.")
            continue

    else:
        print("Invalid choice")
        continue

    if "hello" in user:
        response = "Hello! How can I help you?"

    elif "time" in user:
        response = f"The time is {datetime.now().strftime('%I:%M %p')}"

    elif "date" in user or "today" in user:
        response = f"Today is {datetime.now().strftime('%d %B %Y')}"

    elif "open" in user:
        website = user.replace("open", "").strip()
        response = f"Opening {website}"
        webbrowser.open(f"https://www.{website}.com")

    elif "who are you" in user:
        response = "I am your AI Voice Assistant."

    elif "how are you" in user:
        response = "I am fine. Thank you for asking."

    elif "thank you" in user:
        response = "You are welcome."

    elif "goodbye" in user or "bye" in user:
        response = "Goodbye! Have a nice day"
        print("Bot:", response)
        save_log(user, response)
        engine.say(response)
        engine.runAndWait()
        break

    else:
        try:
          ai_response = model.generate_content(user)
          response = ai_response.text
        except Exception as e:
           print("ERROR:", e)
           response = str(e)

    print("Bot:", response)
    save_log(user, response)

    engine.say(response)
    engine.runAndWait()