import socket

class CacheClient:
    def __init__(host='0.0.0.0', port=11191, protocol='tcp'):
        self.host = host
        self.port = port
        self.protocol = protocol.lower()

        if self.protocol == 'tcp':
            conn_type = socket.SOCK_STREAM
        elif self.protocol == 'udp':
            conn_type = socket.SOCK_DGRAM

        self.sock = socket.socket(socket.AF_INET, conn_type)
        self.sock.connect((self.host, self.port))

    def sendReques(self, req):
        if self.protocol == 'tcp':
            sock.sendall(bytes(data + "\n", "utf-8"))
        elif self.protocol == 'udp':
            sock.sendto(bytes(data + "\n", "utf-8"), (self.host, self.port))
    
    def getData(self):
        received = str(sock.recv(1024), "utf-8")
        
        return received
    
    def getData(self, key):
        pass
    
    def setData(self, key, value, timeout, private):
        pass
    
    def cleanUp(self):
        pass
    
    def delData(self):
        pass
