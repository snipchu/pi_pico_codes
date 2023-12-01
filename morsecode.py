# made on 11/30/23!!
from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT)
led.value(0)

morsekeys = {
    "a": "sl",
    "b": "lsss",
    "c": "lsls",
    "d": "lss",
    "e": "s",
    "f": "ssls",
    "g": "lls",
    "h": "ssss",
    "i": "ss",
    "j": "slll",
    "k": "lsl",
    "l": "slss",
    "m": "ll",
    "n": "ls",
    "o": "lll",
    "p": "slls",
    "q": "llsl",
    "r": "sls",
    "s": "sss",
    "t": "l",
    "u": "ssl",
    "v": "sssl",
    "w": "sll",
    "x": "lssl",
    "y": "lsll",
    "z": "llss"}

def dash():
    led.value(1)
    sleep(.3)
    led.value(0)
    
def dot():
    led.value(1)
    sleep(.15)
    led.value(0)
    
phrase = ""
while phrase != "exit":
    for letter in phrase:
        if letter in morsekeys:
            morse = morsekeys.get(letter)
            for i in morse:
                dash() if i=="l" else dot()
                sleep(.1)
            sleep(.2)
        else:
            sleep(.4)
    phrase = input("Enter a phrase: ")