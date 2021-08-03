from system_details import sys_name
import pyttsx3
engine = pyttsx3.init()
def output(o):
    """
    gives output as voice or text
    """
    print(f"{sys_name}: {o}")
    engine.say(o);
    engine.runAndWait()