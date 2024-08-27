# This file maps a bind that allows an underscore to be typed
# when pressing space while shift is held down

import keyboard

def underscore():
    keyboard.write("_")

keyboard.add_hotkey('shift+space', underscore)

print("Macro set!")
keyboard.wait('esc')