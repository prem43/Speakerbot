import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Get the available voices
voices = engine.getProperty('voices')

# Set the voice to female (typically the second voice in the list)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am Prem. Please tell me how may I help you")       

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")  # Display the recognized speech
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            try:
                webbrowser.open("https://www.youtube.com")
            except Exception as e:
                print(f"Error opening YouTube: {e}")
                speak("Sorry, I was unable to open YouTube.")
        elif 'tell me about yourself' in query:
            try:
                response = "Myself Prem Ranjan. I am from Patna and I am a Fullstack Developer. Currently, I am pursuing my B.Tech from Gyan Ganga College."
                print(f"Speaking: {response}")  # Print the response to verify
                speak(response)
            except Exception as e:
                print(f"Error speaking about yourself: {e}")
                speak("Sorry, I was unable to provide information about myself.")
                       
        elif 'nice' in query:
                try:
                    response = "Thank you so much."
                    print(f"Speaking: {response}")  # Print the response to verify
                    speak(response)
                except Exception as e:
                    print(f"Error for saying anything: {e}")
                    speak("Sorry, I was unable Say anything.")
        elif 'open google' in query:
            try:
                webbrowser.open("https://www.google.com")
            except Exception as e:
                print(f"Error opening Google: {e}")
                speak("Sorry, I was unable to open Google.")

        elif 'open stackoverflow' in query:
            try:
                webbrowser.open("https://stackoverflow.com")
            except Exception as e:
                print(f"Error opening StackOverflow: {e}")
                speak("Sorry, I was unable to open StackOverflow.")

        elif 'play music' in query:
            try:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(f"Error playing music: {e}")
                speak("Sorry, I was unable to play music.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            try:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            except Exception as e:
                print(f"Error opening VS Code: {e}")
                speak("Sorry, I was unable to open Visual Studio Code.")

        elif 'email to prem' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "8294138828.pr@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")    

        else:
            # This block will execute if no other command matches
            print("Sorry, I didn't understand that. Could you please repeat?")
            speak("Sorry, I didn't understand that. Could you please repeat?")
