import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess

# Initialize speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello, I am your Alexa, created by Brian Arek')
engine.say('What can I do for you?')
engine.runAndWait()

# Function to speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
        pass
    return command

# Function to execute Alexa commands
def run_Alexa():
    command = take_command()
    print("User Command:", command)
    text_display.insert(tk.END, "You: " + command + "\n")
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        print("Playing", song)
        pywhatkit.playonyt(song)
        text_display.insert(tk.END, "Assistant: " + 'Playing ' + song + "\n")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)
        print("Current Time:", current_time)
        text_display.insert(tk.END, "Assistant: " + 'The current time is ' + current_time + "\n")
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print("Info:", info)
        talk(info)
        text_display.insert(tk.END, "Assistant: " + info + "\n")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print("Joke:", joke)
        text_display.insert(tk.END, "Assistant: " + joke + "\n")
    elif 'hello' in command:
        talk('Hi!')
        text_display.insert(tk.END, "Assistant: " + 'Hi!' + "\n")
    elif 'hi' in command:
        talk('Hi, how are you?')
        text_display.insert(tk.END, "Assistant: " + 'Hi, how are you?' + "\n")
    elif 'how are you doing' in command:
        talk('I am doing great, Thanks for asking')
        text_display.insert(tk.END, "Assistant: " + 'I am doing great, Thanks for asking' + "\n")
    elif 'switch off' in command:
        talk('Switching off the PC')
        subprocess.run(["shutdown", "/s", "/t", "1"], shell=True)
        text_display.insert(tk.END, "Assistant: " + 'Switching off the PC' + "\n")
    elif 'bye' in command:
        quit()
    else:
        talk('Please say the command again, I didn\'t get you well.')
        text_display.insert(tk.END, "Assistant: " + 'Please say the command again, I didn\'t get you well.' + "\n")

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
