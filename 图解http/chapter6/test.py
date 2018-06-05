a = '["123"","1"]'
b= list(a)
b[1]="'"
b[6]="'"
b = "".join(b)
print (b)
print (eval(b))
