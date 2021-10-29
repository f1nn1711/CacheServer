import socketserver
import time

cache = {}

class CacheServer:
    def __init__(self, host='0.0.0.0', port=1191):
        self.host = host
        self.port = port

    def start(self):
        print(f'Starting cache server on {self.host}:{self.port}')
        with socketserver.TCPServer((self.host, self.port), RequestHandler) as server:
            server.serve_forever()


class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            print('in loop')
            if not self.rfile.peek():
                break

            data = str(self.rfile.readline().strip())[2:]
            print(data)

            command, data = data.split(':')

            command = command.lower()
            print(command)
            if command == 'set':
                print('in command')
                data = data.split(',')

                timeout = None
                if int(data[2]) != 0:
                    timeout = time.time() + int(data[2])
                
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

s = CacheServer()
s.start()