import socket
import sys
import time
import os
HOST = sys.argv[2]
PORT = int(sys.argv[3])
nodename = sys.argv[1]
# print(HOST,PORT)
if len(sys.argv) != 4:
    print('Incorrect input arguments')
    sys.exit(0)
class Node:
    def client(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (HOST,PORT)
        sock.connect(server_addr)
        while True:
            # print('abc')
            for line in sys.stdin:
                print(line)
                data = [line.split()[0],nodename,line.split()[1]]
                # if not data: break
                data = str(' '.join(data))
                sock.sendall(data.encode())
            sock.close()
        
                


    # def _init_(self):
    #     self.client = client
Node1 = Node()
Node1.client()