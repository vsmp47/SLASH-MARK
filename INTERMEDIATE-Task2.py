import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust the speaking rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said: " + query + "\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble processing your request.")
        return ""

if __name__ == '__main__':
    speak("Hi there! I'm Amigo. How can I help you?")

    while True:
        query = listen()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(result)
        elif 'are you' in query:
            speak("I am Amigo, created by Jaspreet Singh.")
        elif 'open' in query:
            if 'youtube' in query:
                speak("Opening YouTube...")
                webbrowser.open("https://www.youtube.com")
            elif 'google' in query:
                speak("Opening Google...")
                webbrowser.open("https://www.google.com")
            elif 'github' in query:
                speak("Opening GitHub...")
                webbrowser.open("https://github.com")
            elif 'stackoverflow' in query:
                speak("Opening Stack Overflow...")
                webbrowser.open("https://stackoverflow.com")
            elif 'spotify' in query:
                speak("Opening Spotify...")
                webbrowser.open("https://www.spotify.com")
            elif 'whatsapp' in query:
                speak("Opening WhatsApp...")
                os.startfile("C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            elif 'music' in query:
                speak("Opening music...")
                webbrowser.open("https://www.spotify.com")
            elif 'disk' in query:
                if 'd' in query:
                    speak("Opening local disk D...")
                    os.startfile("D:\\")
                elif 'c' in query:
                    speak("Opening local disk C...")
                    os.startfile("C:\\")
                elif 'e' in query:
                    speak("Opening local disk E...")
                    os.startfile("E:\\")
        elif 'sleep' in query:
            speak("Goodbye!")
            break
