from output_module import output
import datetime
def greet():
    """
    Wishes user and introduces itself
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        output("Good Morning")
    elif hour >=12 and hour <18:
        output("Good Afternoon")
    else:
        output("Good Evening")