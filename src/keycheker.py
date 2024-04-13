from pynput import keyboard
from app import app
from keyboardList import keyboardMac


def on_press(key):
        print(str(key))
        if str(key) in keyboardMac.keys():
            try:
                app.keyDisplay1(keyboardMac[str(key)][3], keyboardMac[str(key)][4], keyboardMac[str(key)][5], keyboardMac[str(key)][6])
            except AttributeError:
                app.keyDisplay1(keyboardMac[str(key)][3], keyboardMac[str(key)][4], keyboardMac[str(key)][5], keyboardMac[str(key)][6])


def on_release(key):
        if str(key) in keyboardMac.keys():
            app.keyDisplay(keyboardMac[str(key)][3], keyboardMac[str(key)][4], keyboardMac[str(key)][5], keyboardMac[str(key)][6], keyboardMac[str(key)][0])


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()
app.mainloop()
listener.stop()
