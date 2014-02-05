# -*- coding: UTF-8 -*-
#!/usr/bin/env python

# a working main to add on to as we complete each step in the process
# will eventually be removed 

import sys, norm, re 

# currently not functional, I'm getting strange character results. 
# possbiliities: issues with ascii encoding/python version/missign something
# in normalize. 

text = open("../assets/arabic_sources/DhahabiSAN.txt", 'r')
for line in text:
		my_line = norm.rawText(line)
text.close() 
