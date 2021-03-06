#File: parseTest.py
#Given a string with words split by spaces, find the number of occurences
#of a word containing identical characters (in any order) 
#example: foo and oof contain the same characters the same number of times

import timeit
import hashlib

#define the number of times to run the function for benchmarking
number_of_runs = 100000

#this method will sort each word to count the number of occurences
def sortMethod(input_string):

	word_count = {}
	string_list = input_string.split(' ')
	
	for i, word in enumerate(string_list):
	
		string_list[i] = ''.join(sorted(word))
		
		if string_list[i] in word_count:
			word_count[string_list[i]] += 1
		else:
			word_count[string_list[i]] = 1
	
	#print word_count

#this method will hash a unique value for each char in a word, then sum them together, to use as a unique value
def hashMethod(input_string):

	word_count = {}
	string_list = input_string.split(' ')

	for i, word in enumerate(string_list):
	
		word_hash = 0
		#find some unique value to represent the word
		for char in word:
			word_hash += int(hashlib.md5(char).hexdigest(), 16)

		if word_hash in word_count:
			word_count[word_hash] += 1
		else:
			word_count[word_hash] = 1

	#print word_count
	
#call our function to check the string
timeTest = (timeit.Timer(stmt="sortMethod('foo ofo oof si is')", setup = "from __main__ import sortMethod"))
print (timeTest.timeit(number=number_of_runs))

#call our function to check the string
timeTest = (timeit.Timer(stmt="hashMethod('foo ofo oof si is')", setup = "from __main__ import hashMethod"))
print (timeTest.timeit(number=number_of_runs))
