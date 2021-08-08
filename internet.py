from os import replace
import urllib.request
import wikipedia
import webbrowser
from database import get_web_dir
def internet_access():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
def check_wikipedia(query):
    query = query.lower()
    query = query.replace("who is","")
    query = query.replace("what is","")
    query = query.replace("do you know","")
    query = query.replace("tell me about","")
    query = query.strip()
    try:
        data = wikipedia.summary(query, sentences=2)
        return "wikipedia says, "+data
    except Exception as e:    
        return ""
def open_web(query):
    site = query.replace("open ","")
    webdir = dict(get_web_dir(site))
    if(bool(webdir)):
        return webbrowser.open_new_tab(webdir[site])
    else:
        return False


