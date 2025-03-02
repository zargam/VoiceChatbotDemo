from flask import Flask, jsonify
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3
import multiprocessing
import webbrowser

app = Flask(__name__)
CORS(app)

pages = {
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com",
    "youtube": "https://www.youtube.com",
    "instagram":"https://www.instagram.com"
}
keys = pages.keys()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def SpecificWordFromString(string):
    for word in keys:
     if string is not None:
      if string.lower().find(word.lower()) != -1:
       return word   

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        #speak("Hi, I'm Mastix, your AI assistant. How can I help you today?")
        process = multiprocessing.Process(target=speak, args=("Hi, I'm Mastix, your AI assistant. How can I help you today?",))
        process.start()
        process.join()
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-IN").lower()
            #if "Are you here me" in command  or "Can you hear me" in command or "Can you listen to me" in command or "Are you hearing me" in command:
            return command
             #print(f"User said: {command}")
            
        except sr.UnknownValueError:
            process = multiprocessing.Process(target=speak, args=("Sorry, I could not understand.",))
            process.start()
            process.join()
            return "Sorry, I could not understand"
        except sr.RequestError:
            process = multiprocessing.Process(target=speak, args=("Could not request results, please check your internet connection.",))
            process.start()
            process.join()
            return "Could not request results, please check your internet connection"

@app.route('/voice-command', methods=['GET'])
def voice_command():
    command = listen_command()    
    key = SpecificWordFromString(command)
    if key == None:
        #speak("We are sorry, the page you\'re requesting is not in our database",)
        process = multiprocessing.Process(target=speak, args=("We're sorry, the page you're requesting is not in our database",))
        process.start()
        process.join()
        return jsonify({"status": "error", "msg":"We're sorry, the page you're requesting is not in our database","command":command})
    else:
        #speak('Please have some patience, we are redirecting you, thank you')
        #webbrowser.open(pages[key])
        process = multiprocessing.Process(target=speak, args=("Please have some patience, we are redirecting you, thank you",))
        process.start()
        process.join()
        webbrowser.open(pages[key])
        return jsonify({"status": "success", "msg":"Please have some patience, we are redirecting you, thank you","command":command})
    

if __name__ == "__main__":
    app.run(debug=True)
