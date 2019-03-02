# string = input("Enter string:")
# if (string==string[::-1]):
#       print("This word is a palindrome")
# else:
#       print("This word is not a palindrome")
import sys

string = input("Enter your word:")
for x in range(0, len(string)):
	character1 = string[x]
	character2 = string[len(string)-x-1]
	if character1 != character2:
		print("The word is not a palindrome")
		sys.exit(0)
	if character1 == character2:
		continue
print("This word is a palindrome")
