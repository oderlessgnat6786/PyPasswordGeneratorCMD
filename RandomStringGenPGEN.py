import string    
import random
from tkinter import ttk
from tkinter import *


def generateString(S):
    ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = S))
    return str(ran)
    


def ABCabcABCabc(stringg):
    strings = [stringg,stringg.lower()]
    string = ''.join(strings)
    return string

def popup(text1, text2):
    window = Tk()
    top = Toplevel(window)
    top.geometry("750x720")
    top.title("Information")
    Label(top,text = text1, font=('Mistral 18 bold')).place(x=150,y=80)
    Label(top,text = text2, font=('Mistral 18 bold')).place(x=150,y=100)
    window.mainloop()

    
def ReadInfo(name,password):
    print("-----  INFO  -----")
    print("PASSWORD NAME :- ",name)
    print("PASSWORD :- ",password.read())
    

    
