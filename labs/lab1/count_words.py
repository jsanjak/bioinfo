#!/usr/local/bin/python

gpl = open("gpl-3.0.txt").read()

punctuations = "~!@#$%^&*()-/?><,.{}][`'"
transdict={}
for punct in punctuations:
	transdict[punct] =' '

fin = gpl.casefold().translate(str.maketrans(transdict)).split()
