import random
import numbers
import warnings
name = input("Chatbot > What is your name?\nNameless User 1 > ")
questions = ["What is your favorite food?", "How old are you?", "Do you like sweets?"]
question = random.choice(questions)
print("Chatbot > " + question)
answer = input(name + " > ")
if question == questions[0] :
    food = answer
elif question == questions[2] and answer == "yes" or answer == "no" :
    if answer == "yes":
        sweetslike = True
    else:
        sweetslike = False
else:
    try:
        if question == questions[1] and isinstance(int(answer), numbers.Number):
            age = answer
    except:
        print("That answer doesn't make sense!")