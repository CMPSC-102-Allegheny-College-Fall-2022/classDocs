#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DATE = "9 November 2022"
VERSION = "0.3.0"
AUTHOR = "Oliver Bonham-Carter"
AUTHOREMAIL = "obonhamcarter@allegheny.edu"

'''
Detail = Program to emulate a simple conversation. Two speakers (Alice and Bob) exchange strings where a word is common to both. This emulates an initial conversation and a response.
'''


aliceVocab_list = ["I like cats", "I like dogs", "I like rabbits", "I gave carrots to horses","I live on a farm", "I know the farm life", "I have three dogs", "I write my emails each morning.", "My life is all about the country side!"]

bobVocab_list = ["I have two cats", "I have two dogs and a cat", "I know several rabbits","I love carrots", "I love horses","I also live on a farm", "I walk dogs each morning","I have a new email", "I know my garden grows carrots", "My life is all about the country side, too!"]

stopWords_list =["I", "have","know", "like", "love", " to ", " a "]
# we remove stop words as they do not add specificity to the strings

def removeStopWords(in_str):
	""" used to remove the words which do not add to the meaning of the calls and responses"""
	for s in stopWords_list:
		in_str = in_str.replace(s,"")
	# print("removeStopWords(), return statement: ",in_str,type(in_str) )
	return in_str.strip() # return the line without the stop words to the caller
#end of removeStopWords()



def main(): # driver function of the program

	aliceSays_str = random.choice(aliceVocab_list)# choose some random element from the list
	print("  This is Alice. I say to Bob :", aliceSays_str)
	bobSays_str = ""
	aliceSays_list = aliceSays_str.split() # make a list of word from statement
	aliceSays_str = removeStopWords(aliceSays_str)
	while bobSays_str == "":
		bobLine_str = random.choice(bobVocab_list) # choose a reply at random; use this statement for the conversation
		bobLine_i_str = removeStopWords(bobLine_str) # remove the stop words
		bobLine_i_list = bobLine_i_str.split() #make a list from this string and check each word with conditional statements
		for b in bobLine_i_list:
			# print("b = ",b,"  ",aliceSays_list) # what bob think about what to say.
			if b in aliceSays_list:
				#print(" bob says =",b,"  aliceSays_str =",aliceSays_str)
				bobSays_str = bobLine_str

	print("  This is Bob. I reply to Alice :",bobSays_str)
#end of main()


import random
main() # begin the program
