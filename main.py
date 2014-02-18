#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# a working main to add on to as we complete each step in the process
# will eventually be removed 


# NLTK ISRI Stemmer example on sample text. Could replace entire norm.py. 
from nltk.stem.isri import ISRIStemmer

text = open("sample.txt")
stemmer = ISRIStemmer()
for line in text: 
	my_line = stemmer.stem(line) 
	print (my_line) 