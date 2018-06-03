# a = range(10)
# print (a)

# a = enumerate(range(10))
# print (a)

# a = [1, 5, 3]
# b = [1, 4]
# d = {1: "1"}
# c = 1 in d
# print (a>b)


# a = sum((range(101)))
# print (a)

# a = [4, 0, 3, -13, 9, 8, 6]
# print (a,'1111111111111111')

# b = len(a)
# print (b)
# for i in range(0, b):
# 	for j in range(i+1, b):
# 		print (i, j)
# 		if a[i] > a[j]:
# 			a[i], a[j] = a[j], a[i]
# print (a,'22222222222222222')

# #有默认值的参数必须生命在没有默认值的参数之后
# def a(x,y=10):
# 	return x+y

# print (a(5))

# def a(x,y,z):
# 	print (x, '  ', y, '  ', z)
# 	return x+y+z
# print (a(y=2,x=1,z=3))

a = '123'
a = list(a)
a = list(reversed(a))
print (''.join(a))

# a = ['1','2','3']
# a = ''.join(a)
# print (a)
def fanzhuan(a):
	a = a.split(' ')
	b = []
	for word in a:
		word = word[::-1]
		b.append(word)
	return ' '.join(b)

# a = input('>')

# print (fanzhuan(a))


a = [1,2,3,4]
print (a[::-1])

import time

a = time.time()
print (a) 

class a(object):
	print ('111111')

b = a()