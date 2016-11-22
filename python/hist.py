def histogram(string):
	'prints the frequency of characters in a given string'
	d = {}
	for char in string:
		if char.isspace():
			char = '\\n'
		if char.isupper():
			char = char.lower()
		try: 
			d[char] += 1
		except KeyError:
			d[char]  = 1
	
	#now, to print and (try) to prettify the histogram output
	print("{}Frequency of characters{}".format('-'*5, '-'*5))
	print("Character\tFrequence\tCount")
	rankbyOrder(d)

def rankbyOrder(dict):
	'rank frequency from least to most frequent'
	ranking = []
	for entry in dict:
		ranking.append((dict[entry], entry))
	ranking.sort(reverse=True)
	for freq, word in ranking:
		print("{}: {}, {}".format(word, '+'*freq, freq))
		
def hasUpper(string):
	'tests if AT LEAST one character in string is upper-cased'
	for c in string:
		if c.isupper():
			return True
	return False
	
def wordstagram(string):
	'histogram of word frequency'
	#create a list of words to be parsed by histogram
	wordlist = string.split()
	#set a dictionary
	dict = {}
	#iterate through the list
	for word in wordlist:
		if hasUpper(word):
			word = word.lower()
		try:
			dict[word] += 1
		except KeyError:
			dict[word]  = 1
	
	#finally, print results
	print("{}Frequency of Words{}".format('-#-'*5, '-#-'*5))
	print("Word\t\tCount")
	for word in dict:
		print("{}: {}, {}".format(word,'+'*dict[word],dict[word]))
		
		
