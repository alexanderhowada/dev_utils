import pynput
import os
from pynput import keyboard

kc = keyboard.Controller()

def press_enter():
    kc.write("\n")

def string_to_cursor(string_to_type):
    for c in string_to_type:
        if c == '\n':
            print("New line?")
        kc.tap(c)


