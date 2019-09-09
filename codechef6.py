x=int(input())
for _ in range(x):
	y=int(input())
	y=y-2
	z=int(y/2)
	ans=0
	while z>0:
		ans=ans+z
		z=z-1
	print(int(ans))

