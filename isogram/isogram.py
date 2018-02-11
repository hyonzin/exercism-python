def is_isogram(string):
	string = string.replace("-", "").replace(" ", "").lower()
	length = len(string)
	for i in range(length):
		for j in range(i+1, length):
			if string[i] == string[j]:
				return False
	return True

