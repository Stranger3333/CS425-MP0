import socket
import sys
import time
import os
HOST = '127.0.0.1'
PORT = 5566
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