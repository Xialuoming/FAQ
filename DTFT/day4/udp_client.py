#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1'
PORT = 3434

#AF_INET说明使用IPv4地址，SOCK_DGRAM指明UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'Hello world'
s.sendto(data, (HOST, PORT))
print 'Sent: %s to %s' % (data, (HOST, PORT))

s.close()