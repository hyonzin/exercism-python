def is_pangram(sentence):
	sentence = sentence.lower()
	for i in range(26):
		if sentence.count(chr(97+i)) == 0:
			return False
	return True

