import os
import platform
from input_module import take_input
from process_module import process
from output_module import output
from greeting_module import greet

# clear screen before starting
if(platform.uname().system == 'Windows'):
    # Windows
    os.system("cls")
elif(platform.uname().system == 'Darwin' or platform.uname().system == 'linux'):
    # Mac and linux
    os.system("clear")
greet()
while (True):
    i = take_input()
    o = process(i)
    output(o)   
