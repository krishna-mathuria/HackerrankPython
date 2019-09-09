from collections import Counter
x=int(input())
for _ in range(x):
	y=input()
	col_count = Counter(y)
	print(col_count["4"])

