# python2
#!usr/bin/env python
# -*- coding: utf-8 -*-

try:
	mylist = [1, 2]
	e = ''
	print (mylist[3])
	print ('11111111111111')
except ((IndexError,EOFError), e):
	print ('Excption happend')
	print (e)
finally:
	print ('222222222222222')


import sys
class MyError(Exception):
	def __str__(self):
		return "I'm a self-defined Error"

def main():
	try:
		print 'start of main()'
		if len(sys.argv) == 1:
			raise MyError()
		print 'End of main()'
	except MyError, e:
		print e

if __name__ == '__main__':
	main()

class Myclass(object):
	message = 'Hello, Developer!'

	def show(self):
		print self.message

	def __init__(self):
		print '11111111111111111'

inst = Myclass()
inst.show()