import pyttsx3 ##Text to speech conversion library
import speech_recognition as sr ## It will convert speech to text
import datetime
import wikipedia
import webbrowser
import os

def speak(audio):
    print("Speaking:", audio)
    speech_engine=pyttsx3.init('sapi5')
    voices=speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voices[0].id)
    speech_engine.say(audio)
    speech_engine.runAndWait()
    speech_engine.stop()
    print("Speech completed")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! I am siri mam please let me know how can i help you:")

    elif hour>=12 and hour<18:
        speak("Good afternoon! I am sandy please let me know how can i help youu:")

    else:
        speak("Good evening mam! I am janky please let me know how can i help youu?:")

    speak("I am siri mam please let me know how can i help you")

def takecommand():
    #It takes microphone input from the user and returns string output

    r= sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takecommand().lower()
        if 'hello' in query:
            speak("Hello! How can i help you?..")

        #Logic for executing tasks based on query
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')

            search_query=query.replace("wikipedia", "")
            search_query=search_query.replace("search", "")
            search_query=search_query.replace("about", "")
            search_query=search_query.strip()

            try:
                results=wikipedia.summary(search_query, sentences=2)
                print(results)
                speak("According to wikipedia")
                speak(results)

            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results for that topic. Please be more specific.")

            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find that topic on wikipedia.")

            except Exception as e:
                print("Wikipedia error:", e)
                speak("Sorry I could not search wikipedia reight know??")
            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = ""
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            print("Time command detected")
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The time is {strTime}")
            speak(f"Mam, the time is {strTime}")
            print("The time response completed")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Mam, Today's date is {strDate}")

        elif 'open code' in query:
            codepath=""
            os.startfile(codepath)

        elif 'search' in query:
            search_query=query.replace('search','').strip()
            speak(f"searching for{search_query}")
            webbrowser.open("https://www.google.com/search?q=" + search_query)
