from concurrent.futures import thread
from distutils.command.build_scripts import first_line_re
import socket
import sys
import time
import os
from _thread import *
import threading

from cv2 import add

HOST = '127.0.0.1'
PORT = int(sys.argv[1])
Threadnum = 0
# print(str(sys.argv[1]))
if len(sys.argv) > 2:
    print('Incorrect input arguments')
    sys.exit(0)

def nodenum():
    print('abc')
class server:
    
    def multinode(self,connection, addr,Threadnum):
        
        node_connected = connection.recv(1024).decode('utf8').split()
        print(node_connected[0],'-','node'+str(Threadnum),'connected')
        with connection:
            print('Connected by', addr)
            while True:
                # print('waiting for nodes connection....')
                data = connection.recv(1024).decode("utf-8").split()
                print(data[0], 'node'+str(Threadnum),data[1])
        connection.close()
        
    def server_conn(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (HOST, PORT)
        sock.bind(server_addr)
        sock.listen(1)
        global Threadnum
        while True:
            client_conn,client_addr = sock.accept()
            addr_para = client_addr[0]
            # print(addr_para, client_conn)
            x = threading.Thread(target=self.multinode,args=(client_conn,addr_para,Threadnum+1,))
            Threadnum+=1
            x.start()
        sock.close()
Logger = server()
Logger.server_conn()





