#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def fbis(num):
	result = [0, 1]
	for i in range(num - 2):
		result.append(result[-2] + result[-1])
	return result


def main():
	result = fbis(10)
	fobj = open('C:\\Users\\Administrator\\DTFT\\result.txt', 'w+')
	#enumerate()生成带索引的迭代序列
	for i, num in enumerate(result):
		print ("第%d个数是：%d" % (i, num))
		fobj.write("%d " %num)
		time.sleep(0.3)

if __name__ == '__main__':
	main()