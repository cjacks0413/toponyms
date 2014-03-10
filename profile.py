# Creates Ngram Profile for a text 

placeHolder = "__"

def replaceToponyms(text, topList): 
	# scan text and replace all toponym with placeholder 
	# returns new text 

def collectNgrams(text): 
	# find bigrams and trigrams before placeHolder
	# return ngrams as frequency list 

def assess(ngrams): 
	# assess the ngram suspects
	# calls total Freq
	# calls utility and sorts the ngram suspects accordingly. 
	# returns a list of "positive" ngrams 

def totalFreq(ngrams, text): 
	# takes a list of ngram suspects and returns a frequency list of all 
	# of its occurences in the text 

def utility(topFreq, totalFreq): 
	# utility function that determines the value of an ngram given its
	# toponym frequency and total frequency.

## MAIN; as yet undefined . 
# text = replaceToponyms 
# suspects = collectNgrams 
# profile = assess(suspects)


