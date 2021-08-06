import speech_recognition as sr
from internet import internet_access

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        msg = ': Listening....'
        print(msg, end='')
        print('\b' * len(msg), end='', flush=True)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        msg2 = ': Recognizing...'
        print(msg2, end='')
        print('\b' * len(msg2), end='', flush=True)
        query = r.recognize_google(audio,language='en-in')
        print(f"Me: {query}\n")

    except:
        return ""

    return query.lower()

def take_input():
    """
    Takes user input
    """
    if internet_access():
        return TakeCommand()
    else:
        print()
        i = input("Me:")
        return i