# -*- coding: utf-8 -*-

from socket import socket

socket1 = socket()
port = 12345

socket1.connect(("127.0.0.1", port))
print('start Socket client ...')
msg = socket1.recv(1014).decode('utf-8')
print("client receive message={0}".format(msg))
socket1.close()


