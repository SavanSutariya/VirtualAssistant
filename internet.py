from os import replace
import urllib.request
import wikipedia
import webbrowser
from database import get_web_dir,add_web_dir
from gui.input_module import gui_input
from output_module import output
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
        output('Opening '+site)
        return webbrowser.open_new_tab(webdir[site])
    else:
        return False
def add_new_web_address():
    output('Enter site name')
    site_name = gui_input('Site Name')
    output('Enter site address')
    site_address = gui_input('Site Address')
    if(site_name.replace(' ','') == '' and site_address.replace(' ','') == ''):
        return "Both the fields are required"
    else:
        return add_web_dir(site_name,site_address)