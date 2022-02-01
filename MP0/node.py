import socket
import sys
import time
import os
HOST = sys.argv[1]
PORT = int(sys.argv[2])
print(HOST,PORT)
class Node:
    def client(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (HOST,PORT)
        sock.connect(server_addr)
        while True:
            # print('abc')
            for line in sys.stdin:
                print(line)
                sock.sendall(line.encode())
        
                


    # def _init_(self):
    #     self.client = client
Node1 = Node()
Node1.client()