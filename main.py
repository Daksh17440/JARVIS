import pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
from playsound import playsound
import random
import pyautogui
import tkinter as tk
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


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

    speak("I am Jarvis ,boss. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\t")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            if ('salman khan' in query) or ('ranvir singh' in query) or ('varun dhawan' in query) or (
                    'bhat' in query) or ('rhea' in query) or ('deepika' in query) or ('kapoor' in query) or (
                    'akshay kumar' in query) or ('pannu' in query):
                speak(
                    "Sorry fella, i can't tell you anything related to criminals as the info is 99.9 percent fake, feel ashamed of yourself that you are asking about this inhuman")
            else:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=7)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                speak("anything else...")

        elif 'repeat' in query:
            query = query.replace("repeat", "")
            speak(query)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            speak("have a safe browsing!!")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("welcome to stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open flappy' in query:
            speak("opening flappy rora ,the first ever game by rora industries")
            os.startfile("C:\\Users\\hp\\Desktop\\RORAindustries\\flappy rora\\FlappyRORA.exe")

        elif 'open snake with rora' in query:
            speak("opening snake with rora- alpha version,the second game by rora industries")
            os.startfile("C:\\Users\\hp\\Desktop\\RORAindustries\\snake with rora\\Snake with RORA.py")

        elif 'joke' in query:
            jks = pyjokes.get_joke()
            print(jks)
            speak(jks)

        elif 'play gayatri mantr' in query:
            speak("playing gayatri mantra")
            music_dir = "D:\\bhajans\\GAYATRI MANTRA.mp3"
            playsound(music_dir)

        elif 'play hanuman chalisa' in query:
            speak("playing hanuman chalisa")
            music_dir2 = "D:\\bhajans\\HANUMAN CHALISA.mp3"
            playsound(music_dir2)

        elif 'play vishnu' in query:
            speak("playing vishnu sahasnama")
            music_dir3 = "D:\\bhajans\\VISHNU SAHASNAM.mp3"
            playsound(music_dir3)

        elif 'play music' in query:
            n = random.randint(0, 8)
            print(n)
            music_dir6 = "C:\\Users\\hp\\Music\\music\\Ed Sheeran - Shape of You (Official Music Video).mp3"
            music_dir7 = "C:\\Users\\hp\\Music\\music\\Imagine Dragons - Thunder.mp3"
            music_dir8 = "C:\\Users\\hp\\Music\\music\\Imran Khan - Satisfya (Official Music Video).mp3"
            music_dir9 = "C:\\Users\\hp\\Music\\music\\KSHMR, Jeremy Oceans - One More Round (Free Fire Booyah Day Theme Song) [Official Music Video].mp3"
            music_dir10 = "C:\\Users\\hp\\Music\\music\\La Casa De Papel - Bella Ciao [Lyrics] (Money Heist).mp3"
            music_dir11 = "C:\\Users\\hp\\Music\\music\\La Casa de Papel Parte 4 _ Berlín canta Ti Amo _ Netflix.mp3"
            music_dir12 = "C:\\Users\\hp\\Music\\music\\Major Lazer - Cold Water (feat. Justin Bieber & MØ) (Official Dance Video).mp3"
            music_dir13 = "C:\\Users\\hp\\Music\\music\\Ricky Martin - Un, Dos,Tres, Maria.mp3"
            sung = music_dir6, music_dir7, music_dir8, music_dir9, music_dir10, music_dir11, music_dir12, music_dir13
            print(sung)

            playsound(song[n])

        elif 'open minecraft' in query:
            speak("opening minecraft")
            speak("hope you mine some ancient debris today!")
            os.startfile("C:\\Users\\hp\\AppData\\Roaming\\.minecraft\\TLauncher.exe")

        elif 'open epic games' in query:
            speak("launching epic games")
            os.startfile(
                "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")

        elif 'unreal engine' in query:
            speak("opening the world's best game developing engine")
            os.startfile("D:\\UE_4.26\\Engine\\Binaries\\Win64\\UE4Editor.exe")

        elif 'open valorant' in query:
            speak("opening valorant")
            os.startfile("C:\\Riot Games\\VALORANT\\live\\VALORANT.exe")

        elif 'open WhatsApp' in query:
            speak("opening WhatsApp")
            os.startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\app-2.2100.7\\WhatsApp.exe")

        elif 'open bluej' in query:
            speak("opening bluej....PROGRAM WELL")
            os.startfile("C:\\Program Files\\BlueJ\\BlueJ.exe")

        elif 'csgo' in query:
            speak("opening csgo")
            os.startfile("D:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe")

        elif 'war robots' in query:
            speak("opening war robots")
            os.startfile("D:\\SteamLibrary\\steamapps\\common\\War Robots\\WarRobots.exe")

        elif 'jurrasic world' in query:
            speak("opening time waste")
            os.startfile("D:\\JurassicWorldEvolution\\JWE.exe")

        elif 'alien isolation' in query:
            speak("opening alien isolation")
            os.startfile("D:\\AlienIsolation\\AI.exe")

        elif 'steam' in query:
            speak("launching steam")
            os.startfile("C:\\Program Files (x86)\\Steam\\steam.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open python' in query:
            codePath = (
                "C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit).lnks")
            os.startfile(codePath)

        elif ('close' in query) or ('no thanks' in query) or ('exit' in query) or ('mar' in query):
            speak("Thanks ,it was a pleasure helping you")
            sys.exit()