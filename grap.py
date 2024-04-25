import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello I am your Alexa, created by Brian Arek')
engine.say('What can I do for you')
engine.runAndWait()

# Function to speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
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

# Function to execute Alexa commands
def run_Alexa():
    command = take_command()
    print(command)
    text_display.insert(tk.END, "You: " + command + "\n")
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
        text_display.insert(tk.END, "Assistant: " + 'playing' + song + "\n")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is' + time)
        print(time)
        text_display.insert(tk.END, "Assistant: " + 'The current time is' + time + "\n")
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        text_display.insert(tk.END, "Assistant: " + info + "\n")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
        text_display.insert(tk.END, "Assistant: " + joke + "\n")
    elif 'hello' in command:
        talk('Hi!')
        text_display.insert(tk.END, "Assistant: " + 'Hi!' + "\n")
    elif 'hi' in command:
        talk('hi, how are you')
        text_display.insert(tk.END, "Assistant: " + 'hi, how are you' + "\n")
    elif 'how are you doing' in command:
        talk('am doing great, Thanks for asking')
        text_display.insert(tk.END, "Assistant: " + 'am doing great, Thanks for asking' + "\n")
    elif 'bye' in command:
        quit()
    else:
        talk('please say the command again, I didnt get you well')
        text_display.insert(tk.END, "Assistant: " + 'please say the command again, I didnt get you well' + "\n")

# Create GUI window
root = tk.Tk()
root.title("Alexa Assistance")

# Create text display
text_display = tk.Text(root, height=10, width=50)
text_display.pack()

# Function to handle button click
def handle_click():
    text_display.insert(tk.END, "\n")
    run_Alexa()

# Create button
button = tk.Button(root, text="Speak", command=handle_click)
button.pack()

# Run GUI
root.mainloop()
