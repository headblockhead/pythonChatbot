#import required packages

import os
from time import sleep

# set variables

answering_mode = False
asking_mode = False
name = "UNNAMED USER"
question_to_response = {"Who are you?": "I am A ChatBot.", "How old are you?": "Infinitely old.", "What is your name?":"Aperture Laboratories Chatbot 01"}

# define functions

def render_bot(response):
    print("Aperture Laboratories Chatbot 01 > " + response)
def get_answer():
    answering_mode = False
    asking_mode = False
    answer = input(name + " > ")
    if answer == "quit" or answer == "Quit":
        exit()
    return answer
def logo() :
    print("              .,-:;//;:=,")
    print("          . :H@@@MM@M~H/.,+%;,")
    print("       ,/X+ +M@@M@MM%=,-%HMMM@X/,")
    print("     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-")
    print("    ;@M@@M- XM@X;. -+XXXXXHHH@M@M~@/.")
    print("  ,%MM@@MH ,@%=             .---=-=:=,.")
    print("  =@~@@@MX.,                -%HX$$%%%:;")
    print(" =-./@M@M$                   .;@MMMM@MM:")
    print(" X@/ -$MM/                    . +MM@@@M$")
    print(",@M@H: :@:                    . =X~@@@@-")
    print(",@@@MMX, .                    /H- ;@M@M=")
    print(".H@@@@M@+,                    %MM+..%~$.")
    print(" /MMMM@MMH/.                  XM@MH; =;")
    print("  /%+%$XHH@$=              , .H@@@@MX,")
    print("   .=--------.           -%H.,@@@@@MX,")
    print("   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.")
    print("     =XMMM@MM@MM~H;,-+HMM@M+ /MMMX=")
    print("       =%@M@M~@$-.=$@MM@@@M; %M%=")
    print("         ,:+$+-,/H~MMMMMMM@= =,")
    print("               =++%%%%+/:-.")

def ask_or_answer() :
    render_bot("Do you want to ask a question?")
    answer = get_answer()
    if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y" or answer == "1":
        return 1
    elif answer == "No" or answer == "n" or answer == "no" or answer == "n" or answer == "0":
        render_bot("Do you want to be asked questions?")
        answer = get_answer()
        if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y" or answer == "1":
            return 2
        else:
            return 3

# get name
render_bot("What is your name?")
name = get_answer()

# Show information


logo()
print("\nWelcome to the aperture science beta chatbot entitative.")
print("Type \"Quit\" to quit.")
print("Type \"Science\" for an inspirational quote\n")
print("Good luck!\n")

# loop the program


while True:
    ask_output = ask_or_answer()
    if ask_output == 1:
        asking_mode = True
        render_bot("Ask Away!")
        answer = get_answer()
        while asking_mode:
            if answer in question_to_response:
                render_bot(question_to_response[answer])
            elif answer == "exit":
                asking_mode = False
            else:   
                render_bot("I Dont understand that Question. If you would like to choose wheather to ask or answer again, type \"Exit\" to exit asking mode.")
                answer = get_answer()
    elif ask_output == 2:
        answering_mode = True
    
    