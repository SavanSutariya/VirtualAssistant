import webbrowser
from time_module import get_time
from database import get_answers_from_memory,insert_question_and_answer,change_assis_name
from output_module import output
from input_module import take_input
from internet import internet_access,check_wikipedia,open_web
from system_control import take_screenshot
from greeting_module import sayGoodBye
import system_details

def process(query):
    """
    Process the query and return output
    """
    answer = get_answers_from_memory(query)
    if query == "":
        return None
    elif 'open' in query:
        if(open_web(query)):
            return None
        else:
            return "Open application Feature Under development"
    elif answer == "get time details":
        return get_time()
    elif answer == "check internet connection":
        if internet_access() == True:
            return "Online"
        else:
            return "Offline"
    elif answer == "change name":
        output("ok what will you call me?")
        temp = take_input()
        if temp == system_details.sys_name:
            return "ok not changing! You are happy with my old name."
        else:
            change_assis_name(temp)
            system_details.sys_name = temp
            return "Now you can call me " + temp
    elif answer == "take screenshot":
        output("Taking Screenshot..")
        try:
            return "Screenshot saved at "+take_screenshot()
        except:
            return(PermissionError)
    elif answer == "exit":
        output(sayGoodBye())
        exit()
    else:
        output("Should I search on wikipedia for it?")
        temp = take_input()
        if "yes" in temp.lower():
            answer = check_wikipedia(query)
            if answer != "":
                return answer
        else:
            output("I don't know this one can you tell me what it actually mean \nstart with it means.. and I will remember for next time")
            ans = take_input()
            if "it means" in ans:
                ans.replace("it means","")
                ans.strip()
                value = get_answers_from_memory(ans)
                if value == "":
                    return "Sorry, can't help with this one"
                else:
                    insert_question_and_answer(query, value)
                    return"ok, i will remember from next time"
            else:
                return "Sorry, can't help with this one"