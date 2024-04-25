import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your Alexa')
engine.say('What can I do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
       with sr.Microphone() as source:
          print("listening...")
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command.lower()
          if 'Alexa' in command:
              command = command.replace('Alexa', '')
              print(command)
    except:
        pass
    return command

def run_Alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hi!')
    elif 'hi' in command:
        talk('hi, how are you')
    elif 'how are you doing' in command:
        talk('am doing great, Thanks for asking')
    elif 'bye' in command:
        quit
    else:
        talk('please say the command again, I didnt get you well')
        
while True:
   run_Alexa()