import win32com.client
import speech_recognition as sr
def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-in")
            print(text)
        except:
            print("Sorry, I did not get that")
    return text
if __name__ == '__main__':
    # speak("hello")
    speak(listen())
    