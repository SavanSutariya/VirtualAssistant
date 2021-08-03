from output_module import output
import datetime
import random
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
def sayGoodBye():
    lst = ['Bye Bye','Bye','See you later','See you soon','have a good day','good bye','Catch you later']
    return random.choice(lst)+"!"