import socket

class CacheClient:
    def __init__(self, host='0.0.0.0', port=1191, protocol='tcp'):
        self.host = host
        self.port = port
        self.protocol = protocol.lower()

        if self.protocol == 'tcp':
            conn_type = socket.SOCK_STREAM
        elif self.protocol == 'udp':
            conn_type = socket.SOCK_DGRAM

        self.sock = socket.socket(socket.AF_INET, conn_type)
        self.sock.connect((self.host, self.port))

    def sendRequest(self, req):
        print(req)
        if self.protocol == 'tcp':
            print('making tcp req')
            self.sock.sendall(bytes(req + "\n", "utf-8"))
        elif self.protocol == 'udp':
            self.sock.sendto(bytes(req + "\n", "utf-8"), (self.host, self.port))
    
    def recieveData(self):
        received = str(self.sock.recv(1024), "utf-8")
        
        return received
    
    def getData(self, key):
        dataString = f'get:{str(key)}'
        self.sendRequest(dataString)

        return self.recieveData()
    
    def setData(self, key, value, timeout, private):
        dataString = f'set:{str(key)},{str(value)},{str(timeout)},{str(private)}'
        self.sendRequest(dataString)
    
    def cleanUp(self):
        pass
    
    def delData(self):
        pass
