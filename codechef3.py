x=int(input())
for _ in range(x):
	a,b=input().split()
	a=int(a)
	b=int(b)
	if a==b:
		print("=")
	elif a>b:
		print(">")
	else:
		print("<")