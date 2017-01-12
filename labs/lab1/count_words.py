#!/usr/local/bin/python
from collections import Counter
import string
f = open("gpl-3.0.txt")
gpl = f.read()
f.close()

transdict={}
for punct in string.punctuation:
	transdict[punct] =None

gpl = gpl.casefold().translate(str.maketrans(transdict)).split()
#gpl = gpl.translate(None,string.punctuation)
#gpl = gpl.lower.split()
counts = Counter(gpl)

ofile = open('output.txt','w')
for a in counts:
	print(a, counts[a])
	ofile.write(a + ': ' + str(counts[a])+ '\n')
ofile.close()

