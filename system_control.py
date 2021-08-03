import pyautogui
import datetime
from settings import settings
import os

def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        location = settings['screenshot_save_location']
        date = datetime.datetime.now().strftime("%Y_%m_%d-%I%M%S_%p")
        if(os.path.exists(location)):
            screenshot.save(location+date+"_screenshot.png")
        else:
            location = os.path.expanduser('~\downloads')+"/screenshots/"
            try:
                os.stat(location)
            except:
                os.mkdir(location)
            screenshot.save(location+date+"_screenshot.png")
        return location
    except:
        raise PermissionError('Cannot take screenshot')

print(take_screenshot())