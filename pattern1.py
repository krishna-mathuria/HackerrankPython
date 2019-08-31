#1
#11
#202
#3003
#40004

n=int(input())
i=1
x=1
while(i<=2):
	j=1
	while(j<=i):
		print("1",end="")
		j=j+1
	print()
	i=i+1
i=3
while(i<=n):
	j=i-1
	print(j,end="")
	while(x<j):
		print("0",end="")
		x=x+1
	print(j,end="")
	print()
	i=i+1
	x=1

