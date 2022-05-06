import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is ' in command:
        person = command.replace('who  is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

   

    elif 'about pc owner' in command:
        talk('his name is akr,he is such good boy for who respect him andd bad for who is troubling')


    elif 'akr' in command:
        talk('he is such good boy for who respect him andd bad for who is troubling')


    elif 'are you single' in command:
        talk('I am in a relationship with AKR Brain')

    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
