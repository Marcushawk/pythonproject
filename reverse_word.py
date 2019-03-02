string = input("Enter your word:")
s = ""
some_array = []
for x in range(0, len(string)):
	character2 = string[len(string)-x-1]
	some_array.append(character2)
print(s.join(some_array))