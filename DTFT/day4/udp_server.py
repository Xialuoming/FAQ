#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

HOST = '0.0.0.0'
PORT = 3434

#AF_INET说明使用IPv4地址，SOCK_DGRAM指明UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
	data, addr = s.recvfrom(1024)
	print 'Received: %s from %s' % (data, addr)

s.close()