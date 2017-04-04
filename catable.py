#!/usr/bin/python

import sys;
import os;

#get arg
filearg = sys.argv[1]

wrappedFileName = 'output.txt'
newlineCharacters = ['\n']





if(not filearg):
	print "Usage: catable.py <file>"
	print "catable takes a file and writes a file (catme.sh) that print the original file to " + wrappedFileName + "."
	print "This is useful if you have access to a remote terminal, but cannot upload a simple file."
else:

	infile = open(filearg,'r');
	outfile = open('catme.sh','w');
	outfile.write('rm ' + wrappedFileName + '; touch ' + wrappedFileName + '\n')
	for line in infile:
		escapedLine = ""
		for char in line:
			if(not char in newlineCharacters):
				escapedLine += '\\' + char

		outfile.write('echo ' + escapedLine + ' >> ' + wrappedFileName + ' \n')
	print 'File has been catabled, check it out at ./catme.sh'
