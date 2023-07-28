import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import pyaudio


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

recognizer= sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearning Background noises....Please wait a second!!')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("Ask me bro...")
        print("I have only these much properties...So be in this area only: ")
        print("1) Can Play songs for your.")
        print("2) Can open Youtube for you")
        print("3) Can open chrome browser for you")
        print("4) Can show current time to you")
        print("That's all for now...Happy using ((:-)")
        p="Hey user, Bits here, watch the above menu and ask me what can I do for you!!"
        engine.say(p)
        engine.runAndWait()
        recordedaudio=recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print(" You said " + format(text))

    except Exception as ex:
        print(ex)

    if 'chrome' in text:
        a="Yeah Dude, fulfilling ur demand.....Happy Happy Happy.."
        engine.say(a)
        engine.runAndWait()
        program="C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    if 'time' in text:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

    if 'play' in text:
        b='Opening your request...have patience....Do not panic at all bro'
        engine.say(b)
        engine.runAndWait()
        pywhatkit.playonyt(text)
        
    if 'youtube' in text:
        c='wowowowo get ready...Youtube is getting ready for you...'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')


while True:
    cmd()






