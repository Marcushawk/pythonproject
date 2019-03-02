asterisks = []
for x in range(0, 5):
	for t in range(0, x+1):
		asterisks.append('*')
	print(''.join(asterisks))
	asterisks = []
for x in range(5, 0, -1):
	for t in range(x, 0, -1):
		asterisks.append('*')
	print(''.join(asterisks))
	asterisks = []