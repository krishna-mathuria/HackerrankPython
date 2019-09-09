x,y=input().split()
x=int(x)
y=float(y)
if x>=y:
	print("{:.2f}".format(y))
else:
	if x%5==0:
		print("{:.2f}".format(y-x-0.50))
	else:
		print("{:.2f}".format(y))
