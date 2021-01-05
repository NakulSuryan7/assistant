import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import os
import weather as wt


from googlesearch import search


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):

    engine.say('i am your wonder women')
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                command = command.replace('hello', '')

                print(command)
    except:
        pass

    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'open notepad' in command:

        subprocess.Popen('notepad.exe')







    elif 'close notepad' in command:
        os.system('TASKKILL /F /IM notepad.exe')

    elif 'close chrome' in command:
        os.system('TASKKILL /F /IM chrome.exe')

    elif 'open chrome' in command:
        print('gfjhfj')
        subprocess.call('chrome.exe')

    elif 'open telegram' in command:
        subprocess.Popen('telegram.exe')







    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i have a headache')

    elif 'are you single' in command:
        talk('i am in a relationship with wifi')

    elif 'weather' in command:

        talk("Where are you now")
        place = command
        wt.main(place)


        temp = wt.current_temperature

        descri = wt.weather_description
        talk("Current Temperature" + str(temp) + "kelvin")
        talk("Current weather is" + descri)

    elif 'what is' in command:
        what = command.replace('what is', '')
        info = wikipedia.summary(what, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())



    elif 'search' in command:

        searched = command.replace('search', '')

        for j in search(searched, tld="com", num=10, stop=10, pause=2):
            print(j)

        talk("Here is the search result")

    else:
        talk('i didnt get that')


while True:
    try:
        run_alexa()
    except:
        print('hey how can i help u')
