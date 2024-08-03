class max3num:
	def __init__(self,a,b,c):
		if(a>b)and(a>c):
			print("A is maximum:",a)
		elif(b>c):
			print("B is maximum:",b)
		else:
			print("C is maximum:",c)
a=int(input("A ="))
b=int(input("B ="))
c=int(input("C ="))
max3num = max3num(a,b,c)
