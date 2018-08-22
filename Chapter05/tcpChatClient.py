# -*- coding: utf-8 -*-

import threading
import socket
import os
import sys
import time

cSocket = socket.socket()
cSocket.connect(('127.0.0.1', 5000))
msg = ' '
running = True

def recvMsg():
    global running

    while running:
        msg_bytes = cSocket.recv(1024)
        msg = msg_bytes.decode('utf8')
        print('\n从服务器端接收的消息: {0}\n'.format(msg) )
        time.sleep(1)

def sendMsg():
    global running
    while running:
        # print('msg')
        msg = input('\n请输入要发送给服务器的消息：')
        msg_bytes = msg.encode('utf8')
        cSocket.send(msg_bytes)

        if msg == "exit":
            running = False
            break

if __name__ == '__main__':
    t1 = threading.Thread(target=recvMsg, args=(), name='recv_thread')
    t2 = threading.Thread(target=sendMsg, args=(), name='send_thread')
    t1.start()
    t2.start()
