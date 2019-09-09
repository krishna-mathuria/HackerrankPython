x,y=input().split()
x=int(x)
y=int(y)
k=0
for _ in range(x):
	z=int(input())
	if z%y==0:
		k=k+1
print(k)