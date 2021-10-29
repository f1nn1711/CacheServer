import socketserver
import time
from sys import getsizeof

cache = {}

class CacheServer:
    def __init__(self, host='0.0.0.0', port=1191):
        self.host = host
        self.port = port

    def start(self):
        print(f'Starting cache server on {self.host}:{self.port}')
        try:
            with socketserver.TCPServer((self.host, self.port), RequestHandler) as server:
                server.serve_forever()
        except Exception as e:
            print(e)
        finally:
            quit()


class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            if not self.rfile.peek():
                break

            data = str(self.rfile.readline().strip())[2:-1]

            command, data = data.split(':')

            command = command.lower()
            data = data.split(',')

            print(command)

            if command == 'set':
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

            elif command == 'get':
                if data[0] not in cache:
                    self.wfile.write(b'Error: Data not in cache')
                    print('not found')
                    print(data[0])
                    continue

                dataFromCache = cache[data[0]]
                if dataFromCache['private'] != False and dataFromCache['private'] != self.client_address[0]:
                    self.wfile.write(b'Error: IP does not have access')
                    print('invalid user')
                    continue
                
                if dataFromCache['timeout'] != None and time.time() > dataFromCache['timeout']:
                    cache.pop(data[0], None)
                    self.wfile.write(b'Error: data has expired')
                    print('timeout')
                    continue

                self.wfile.write(str.encode(dataFromCache['value']))

            elif command == 'cu':
                for key in cache:
                    if cache[key]['timeout'] != None and time.time() > cache[key]['timeout']:
                        cache.pop(data[0], None)

            elif command == 'rm':
                cache.pop(data[0], None)

            elif command == 'sdata':
                dataString = f'Utilization: {getsizeof(cache)} bytes'
                self.wfile.write(str.encode(dataString))

s = CacheServer()
s.start()
