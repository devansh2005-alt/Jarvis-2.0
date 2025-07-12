import pyttsx3
import speech_recognition as sr
import time
import datetime
import wikipedia
import requests
import webbrowser
import subprocess
import pyautogui
import os
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

print("✅ Script started")

engine = pyttsx3.init()
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

import os
import pygame

# Path to your music folder
music_folder = r"C:\Users\devansh\Music\jarvis_music"  # 🔁 Update path if different

pygame.init()
pygame.mixer.init()

music_files = [file for file in os.listdir(music_folder) if file.endswith('.mp3')]
current_index = 0

def play_music():
    global current_index
    if not music_files:
        speak("No music files found.")
        return
    song_path = os.path.join(music_folder, music_files[current_index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    speak(f"Playing {music_files[current_index]}")

def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped.")

def next_music():
    global current_index
    current_index = (current_index + 1) % len(music_files)
    play_music()

def open_website_or_app(command):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "naukri": "https://www.naukri.com",
        "linkedin": "https://www.linkedin.com"
    }

    apps = {
        "vs code": r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe"
    }

    for site in sites:
        if site in command:
            speak(f"Opening {site}")
            webbrowser.open(sites[site])
            return

    for app in apps:
        if app in command:
            speak(f"Launching {app}")
            subprocess.Popen(apps[app])
            return

    speak("Sorry, I don't know how to open that.")

import smtplib

def send_email(to_address, content):
    sender_email = "patidarraj1272@gmail.com"
    app_password = "wmji prsa rxgr ddbl"  # 🔐 16-digit app password

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, to_address, content)
        server.quit()
        speak("Email has been sent successfully.")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")
        print(str(e))

# Contacts dictionary (can be extended)
contacts = {
    "devansh": "patidardevansh44@gmail.com",
    "kunal": "kpatidar0852@gmail.com",
    "benu": "patidarvaishnavi2008@gmail.com"
}

def email_feature():
    speak("To whom should I send the email?")
    recipient = listen().lower()

    if recipient in contacts:
        to_address = contacts[recipient]
        speak("What should I say?")
        message = listen()
        send_email(to_address, message)
    else:
        speak("Sorry, I don't have that contact saved.")

def get_weather(city):
    api_key = "b777b6f913f3bc6f1d61478431739320"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            speak("City not found. Please try again.")
            return

        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        report = f"The weather in {city} is {temp} degrees Celsius with {description}. Humidity is {humidity} percent and wind speed is {wind_speed} meters per second."
        speak(report)

    except Exception as e:
        speak("Sorry, I couldn't fetch the weather.")

try:
    engine = pyttsx3.init()
    print("🔊 TTS engine loaded")
except Exception as e:
    print(f"❌ TTS init error: {e}")

def speak(text):
    print(f"🗣 Speaking: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ Speak error: {e}")

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=0) as source:
            print("🎤 Adjusting for noise...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("🎧 Listening now...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
    except Exception as e:
        print(f"❌ Mic error: {e}")
        return ""

    try:
        command = r.recognize_google(audio)
        print(f"✅ Recognized: {command}")
        return command.lower()
    except Exception as e:
        print(f"❌ Recognition error: {e}")
        return""
import requests

def get_news():
    api_key = "3ce924136e5945c7894b264daf34e692"  # ← replace with your actual key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        articles = data["articles"][:5]  # Top 5 headlines

        news_list = [article["title"] for article in articles]
        return news_list
    except Exception as e:
        print("❌ Error fetching news:", e)
        return ["Sorry, I couldn't fetch the news right now."]
    
def verify_user():
      speak("Please say the password to continue.")
      command = listen().lower()
      if voice_password in command:
       speak("Access granted. Welcome back.")
       return True
      else:
       speak("Access denied. You are not authorized.")
       return False
      

def set_alarm(alarm_time):
    speak(f"Alarm set for {alarm_time}")
    print(f"⏰ Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            speak("Wake up, Devansh! This is your alarm.")
            print("🔔 Alarm ringing...")

            pygame.mixer.init()
            pygame.mixer.music.load("alarm/alarm.mp3")
            pygame.mixer.music.play()

            time.sleep(20)
            pygame.mixer.music.stop()
            break
        time.sleep(10)  # Check every 10 seconds

import geocoder

def get_location():
    try:
        g = geocoder.ip('me')
        city = g.city
        state = g.state
        country = g.country
        location = f"You are in {city}, {state}, {country}."
        speak(location)
        print(f"📍 Location: {location}")
    except Exception as e:
        speak("Sorry, I couldn't fetch your location.")
        print(f"❌ Location Error: {e}")

def take_screenshot():
    try:
        # Create "screenshots" folder if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # Generate a filename with date and time
        filename = datetime.datetime.now().strftime("screenshot_%Y-%m-%d_%H-%M-%S.png")
        path = f"screenshots/{filename}"

        # Take screenshot and save it
        screenshot = pyautogui.screenshot()
        screenshot.save(path)

        speak("Screenshot taken and saved.")
        print(f"✅ Screenshot saved at: {path}")
    except Exception as e:
        speak("Sorry, I couldn't take the screenshot.")
        print(f"❌ Screenshot error:{e}")

def increase_brightness():
    try:
        sbc.set_brightness('+10')
        speak("Increased brightness.")
    except:
        speak("Sorry, I couldn't change the brightness.")

def decrease_brightness():
    try:
        sbc.set_brightness('-10')
        speak("Decreased brightness.")
    except:
        speak("Sorry, I couldn't change the brightness.")

def set_volume(level):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Set volume safely between 0.0 and 1.0
        level = max(0.0, min(level, 1.0))
        volume.SetMasterVolumeLevelScalar(level, None)

        speak(f"Volume set to {int(level * 100)} percent.")
    except Exception as e:
        print(f"Volume Error: {e}")
        speak("Sorry, I couldn't change the volume.")

def open_task_manager():
    subprocess.Popen('taskmgr')
    speak("Opening Task Manager.")

def shutdown_system():
    speak("Shutting down your computer.")
    os.system("shutdown /s /t 1")

def restart_system():
    speak("Restarting your computer.")
    os.system("shutdown/r/t1")

def run_jarvis():
    print("🚀 Jarvis is running")
    speak("Hello, I am Jarvis. Please say something.")

    while True:
        command = listen()

        if not command:
            speak("I didn't hear anything.")
            continue

        command = command.lower()

        if "weather in" in command:
            city = command.split("in")[-1].strip()
            get_weather(city)

        elif "hello" in command:
            speak("Hello! How can I help you?")

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        elif "send email" in command:
            email_feature()

        elif "play music" in command:
         play_music()

        elif "stop music" in command:
         stop_music()

        elif "next song" in command or "next music" in command:
         next_music()

        elif "open" in command or "launch" in command:
         open_website_or_app(command)

        elif "where am i" in command or "my location" in command:
            get_location()
        
        elif "take screenshot" in command or "screenshot" in command:
            take_screenshot()

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "date" in command:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            speak(f"Today is {today}")
            
            query=listen().lower() or ""

       

        elif "who is" in command or "what is" in command or "tell me about" in command:
           try:
                topic = command.replace("tell me about", "").replace("who is", "").replace("what is", "").strip()
                results = wikipedia.search(topic)
                if results:
                    summary = wikipedia.summary(results[0], sentences=2)
                    print(f"📖 Wikipedia summary: {summary}")
                    speak(summary)

                else:
                 speak("Sorry, I couldn't find that on Wikipedia.")
           except Exception as e:
               print(f"❌ Wikipedia error: {e}")
               speak("Sorry, I couldn't fetch the summary.")

        elif "where is" in command:
            try:
                  place = command.replace("where is", "").strip()

                        # Search for best match in Wikipedia
                  results = wikipedia.search(place)

                  if results:
                            # Use best matched result for summary
                              topic = results[0]
                              location_summary = wikipedia.summary(topic, sentences=2)

                            # Speak location description first
                              speak(f"{topic} is located as follows:")
                              speak(location_summary)

                              print(f"📍 Wikipedia: {location_summary}")

                             # Then open Google Maps
                              maps_url = f"https://www.google.com/maps/place/{place.replace(' ', '+')}"
                              speak(f"Opening {place} in Google Maps.")
                              webbrowser.open(maps_url)
                  else:
                      speak("Sorry, I couldn't find that place on Wikipedia.")
            except Exception as e:
             print(f"❌ Location error: {e}")
             speak("Sorry, I couldn't fetch the location.")

        elif "set alarm for" in command:
            try:
                 alarm_time = command.replace("set alarm for", "").strip()
                 set_alarm(alarm_time)
            except Exception as e:
              print(f"❌ Alarm error: {e}")
              speak("Sorry, I couldn't set the alarm.")

        elif "news" in command:
            speak("Here are the latest headlines.")
            headlines = get_news()
            for i, headline in enumerate(headlines, start=1):
              if headline:  # Make sure it's not None or empty
               print(f"{i}. {headline}")
               try:
                 speak(headline[:200])  # Limit to 200 characters
               except Exception as e:
                 print(f"❌ Couldn't speak headline {i}:{e}")

        elif "increase brightness" in command:
         increase_brightness()

        elif "decrease brightness" in command:
          decrease_brightness()

        elif "mute volume" in command:
            set_volume(0.0)

        elif "unmute" in command or "full volume" in command:
               set_volume(1.0)

        elif "increase volume" in command:
               set_volume(0.7)  # Adjust as needed

        elif "decrease volume" in command:
              set_volume(0.3)

        elif "open task manager" in command:
            open_task_manager()

        elif "shutdown the system" in command:
             shutdown_system()

        elif "restart the system" in command:
            restart_system()
                 
        

        elif "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("You said:"+command)

if __name__=="__main__":
    print("main.py is executing")
    voice_password = "hanuman"
    if verify_user():
     run_jarvis()