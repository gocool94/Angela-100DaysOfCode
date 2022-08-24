def hello():
    print("Hello..!!")

hello()


def name(firstname,lastname):

    print(f"{firstname}   {lastname}")

name(lastname="kalivarathan",firstname="gokul")

"""
This coding exercise has two parts:

Create a function, user_name() , which returns the string "Rolf" .
Create a function, greeting() , which takes a name as an argument and returns "Hello, NAME, how are you?" 

"""

def user_name():
    return "Rolf"

def greeting(name):
    print(f"Hello, {name}, how are you?")
