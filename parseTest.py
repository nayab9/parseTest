#File: parseTest.py
#Check a string for words which contain identical characters
#example: foo and oof contain the same characters the same number of times

import timeit

#define the number of times to run the function for benchmarking
number_of_runs = 100000

word_count = {}

def sortMethod(input_string):
	string_list = input_string.split(' ')
	for i, word in enumerate(string_list):
		string_list[i] = ''.join(sorted(word))
		if string_list[i] in word_count:
			word_count[string_list[i]] += 1
		else:
			word_count[string_list[i]] = 1
	#print word_count
	
#call our function to check the string
timeTest = (timeit.Timer(stmt="sortMethod('foo ofo oof si is')", setup = "from __main__ import sortMethod"))
print (timeTest.timeit(number=number_of_runs))
