# -*- coding: UTF-8 -*-
# top_list.py 
# creates Unique Toponym List from tagged text 

import re, norm, sys, os.path 

topTag = re.compile(r'(?<=#TOP).*')
# topAndNisba = re.compile(r'(?<=#TOP).*(?=#NISBA)') 
# nisba = re.compile(r'(?<=#NISBA).*')

# # test = re.findall(topOnly, text.read())
# # for i in test: 
# # 	#print (i)
# # 	foo = i.split('#')[1]
# # 	print (foo)

# print (test)
# print (topList)
# print (len(topList))

topList = ""
for filename in os.listdir("../MB"): 
	if filename.endswith(".alpha"): 
		text = open("../MB/" + filename, "r", encoding='utf-8')
		matches = re.findall(topTag, text.read()) 
		for line in matches: 
			toponym = line.split('#')[1]
			toponym = norm.toRawText(line)
			topList += toponym

topList.split()
topListFile = open("all_toponyms.txt", 'w', encoding='utf-8')
topListFile.write(topList)
print (len(topList))
