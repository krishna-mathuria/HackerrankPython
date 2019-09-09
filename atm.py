x,y=input().split()
x=int(x)
y=float(y)
if  x + 0.50 <= y and x % 5 == 0:
    print("%.2f" %((y - x)- 0.50))
else:
    print("%.2f" %y)