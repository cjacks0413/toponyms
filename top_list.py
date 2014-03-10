# -*- coding: UTF-8 -*-
# top_list.py 
# creates Unique Toponym List from tagged text 

import re, norm, sys, os.path 

topTag = re.compile(r'(?<=#TOP).*')

topList = ""
for filename in os.listdir(sys.argv[1]): 
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
