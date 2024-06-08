import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Function to speak the given text"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen for voice input"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("User said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
        return ""

def main():
    """Main function to run the voice assistant"""
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I assist you?")
        elif "goodbye" in query or "exit" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
