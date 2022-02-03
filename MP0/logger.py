import socket
import sys
import time
import os
from _thread import *
import threading
import csv

# HOST = '172.22.158.15'
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
    def storedata(self,data,width):
        recv_time = time.time()
        gen_time = float(data.split()[0])
        delay = recv_time-gen_time
        newline = data+' '+str(delay)+' '+str(width)
        print(newline)
        return newline.split()

    def multinode(self,connection, addr,Threadnum):
        
        node_connected = connection.recv(1024).decode('utf8').split()
        f = open(node_connected[1]+'.csv','w')
        writer = csv.writer(f)
        # writer.writerow(node_connected)
        # print(node_connected)
        # node_connected = node_connected.split()
        print(time.time(),'-',node_connected[1],'connected')
        with connection:
            # print('Connected by', addr)
            
            while True:
                # print('waiting for nodes connection....')
                data = connection.recv(1024).decode("utf-8")
                if not data: 
                    print(time.time(),'-',node_connected[1],'disconnected')
                    break
                width = len(data)
                line = self.storedata(data,width)
                # f.write(line)
                writer.writerow(line)
                data = data.split()
                print(data[0],data[1],data[2])
        connection.close()
        f.close()
        
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





