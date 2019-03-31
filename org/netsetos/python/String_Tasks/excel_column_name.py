MAX=25
def printString(n):
	string = ["\0"] * MAX

	i= 0

	while (n > 0):

		rem = int(n % 26)
		if (rem == 0):
			string[i] = 'Z'
			i += 1
			n = (n / 26) - 1
		else:
			string[i] = chr((rem - 1) + ord('A'))
			i += 1
			n = int(n / 26)
	string[i] = '\0'

	# Reverse the string and print result
	string = string[::-1]
	print( "".join(string))



printString(78)







