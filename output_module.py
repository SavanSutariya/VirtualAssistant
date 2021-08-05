from system_details import sys_name
from time_module import get_time
import pyttsx3
engine = pyttsx3.init()
def output(o):
    """
    gives output as voice or text
    """
    print(f"{sys_name}: {o} \t[{get_time()}]")
    engine.say(o)
    engine.runAndWait()