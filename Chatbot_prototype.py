#import required packages

import os
from time import sleep

# set variables

name = "UNNAMED USER"
question_to_response = {"Who are you?": "I am A ChatBot.", "How old are you?": "Infinitely old.", "What is your name?":"Aperture Laboratories Chatbot 01"}

# define functions

def render_bot(response):
    print("Aperture Laboratories Chatbot 01 > " + response)
def get_answer():
    answer = input(name + " > ")
    if answer == "quit":
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


# Show information


logo()
print("\nWelcome to the aperture science beta chatbot entitative.")
print("Type \"Quit\" to quit.")
print("Type \"Science\" for an inspirational quote\n")
print("Good luck!\n")

# loop the program

while True:
    render_bot("What is your name?")
    name = get_answer()
    render_bot("Do you want to ask a question?")
    answer = get_answer()
    if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y" or answer == "1":
        render_bot("Ask Away!")
        answer = get_answer()
        render_bot(question_to_response[answer])
