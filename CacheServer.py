import socketserver
import time

cache = {}

class CacheServer:
    def __init__(host='0.0.0.0', port=11191, handler=RequestHandler):
        self.host = host
        self.port = port

        self.server = socketserver.TCPServer((self.host, self.port), handler)
    
    def start():
        self.server.serve_forever()


class RequestHandler(socketserver.StreamRequestHandler):
    def handler(self):
        while True:
            if not self.rfile.peek():
                break

            data = self.rfile.readline().strip()

            command, data = data.split(':')

            command = command.lower()
            if command == b'set':
                data = data.split(',')

                timeout = None
                if data[2] != 0:
                    timeout = time.time() + int(data[0])
                
                private = False
                if data[3] == 'True':
                    private = self.client_address[0]
                
                dataToCache = {
                    "value": data[1],
                    "timeout": timeout,
                    "private": private
                }

                cache[data[0]] = dataToCache

                print(cache)
            elif command == b'get':
                pass
            elif command == b'cu':
                pass
            elif command == b'rm':
                pass