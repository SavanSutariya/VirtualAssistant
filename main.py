import os
from input_module import take_input
from process_module import process
from output_module import output

os.system("cls")
while (True):
    i = take_input()
    o = process(i)
    output(o)   
