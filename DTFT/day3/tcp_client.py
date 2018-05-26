#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 3434

#AF_INET说明使用的是IPv4地址，SOCK_STREAM指明TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
print 'Current %s:%d OK' % (HOST, PORT)
data = s.recv(1024)
print 'Received: ', data
s.close()