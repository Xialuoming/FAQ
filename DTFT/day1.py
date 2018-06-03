#-*- coding: utf-8 -*-
import sys

param = None

if len(sys.argv) > 1:
	param = int(sys.argv[1])

print (sys.argv,'11111111111111')
# sys.argv中的第一个值（索引为0）是Python程序名（day1.py）,
# 从第二个值开始其他元素为字符串类型的控制台输入参数
if param is None:
	print ('The param is not set')

elif param < -10:
	print ('The param is small')

elif param > 10:
	print ('The param is big')

else:
	print ('The param is middle')

#元组变长参数：*，适用于未知参数数量不固定，且函数使用这些
#参数时无须知道参数的名字的场合
def show_message(message, *tupleName):
	for name in tupleName:
		print (message, ',', name)

if __name__ == '__main__':
	show_message('Good morning', 'jack', 'Evans', 893)



#字典变长参数：**，适用于未知参数数量不固定，且函数使用这些
#参数时需要知道参数的名字的场合
#has_key() 为Python2 独有函数
def check_book(**dictParam):
	if dictParam.has_key('Price'):
		price = int(dictParam['Price'])
		if price > 100:
			print ('*********I want buy this book***********')
	print ("The book information are as follow:")
	for key in dictParam.keys():
		print (key, ':', dictParam[key])
	print ('-----------------------------')

if __name__ == '__main__':
	check_book(author = 'James', Title = 'Economics')
	check_book(author = 'Linda', Title = 'Deepin')
	check_book(Date = '2012-3-19', Title = 'Cooking', Price = 110)
	check_book(author = 'James', Price = 120)

#reduce python2函数
print (reduce(lambda x, y: x+y,range(101)))