y = []
x = input()
counter = 0
for i in x:
	y.insert(0,i)
	print(counter)
	counter = counter + 1
print("".join(y))