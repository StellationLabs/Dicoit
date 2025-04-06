import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import wikipedia
import pyjokes

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male voice, 1 for female

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Take voice command from user"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return "None"
    return query.lower()

def greet():
    """Greet the user based on time"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning! I'm Dicoit. How can I help you?")
    elif 12 <= hour < 18:
        speak("Good Afternoon! I'm Dicoit. How can I assist?")
    else:
        speak("Good Evening! I'm Dicoit. What can I do for you?")

def run_dicoit():
    """Main function to run the AI assistant"""
    greet()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'what can you do' in query:
            speak("I can perform various tasks like:")
            print("- Open YouTube/Google\n- Play music/videos\n- Tell time/date\n- Search Wikipedia\n- Tell jokes\n- Answer general questions")
            speak("Open websites, play media, tell time and date, share jokes, and answer questions.")

        elif 'exit' in query or 'goodbye' in query or 'sleep' in query:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I'm sorry, I didn't understand that. Could you please repeat?")

if __name__ == "__main__":
    run_dicoit()