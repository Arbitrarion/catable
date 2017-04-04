#!/usr/bin/python

import sys;
import os;

#global vars
false=bool(0)
true=bool(1)

fileArg = ''
wrappedFileName = 'output.txt'
newlineCharacters = ['\n']
memVar = 'qwymzxxcovi'
printToMemory = false

############################function definitions
def parseArgs():
	if(len(sys.argv) < 2):
		return false
	global fileArg
	fileArg = sys.argv[1]
	for i in range(2, len(sys.argv)):
		if (sys.argv[i] == '-m'):
			print "write to memory enabled"
			global printToMemory
			printToMemory = true;

	return true



def escapeString(line):
	escapedLine = ""
	for char in line:
		if(not char in newlineCharacters):
			escapedLine += '\\' + char
	return escapedLine

def printHeader(outfile):
	if(printToMemory):
		outfile.write(memVar + "=''\n")
	else:
		outfile.write('rm ' + wrappedFileName + '; touch ' + wrappedFileName + '\n')

		#ifelse skasofinA: add file check, abort if not exists
		outfile.write('if [[ ! -a ' + wrappedFileName + ' ]]; then\n')
		outfile.write('\techo "Error writing to file, trying regenerating with the -m flag."\n')
		outfile.write('else\n')
		
def printLine(outfile, escapedLine):
	if(printToMemory):
		toPrint = memVar + '=$' + memVar + '\ ' + escapedLine + '\\;\n'
		outfile.write(toPrint)
	else:
		outfile.write('\techo ' + escapedLine + ' >> ' + wrappedFileName + '\n')

def printFooter(outfile):
	if(printToMemory):
		outfile.write('echo "file written to variable \\$' + memVar + '."\n')
	else:
		#endif skasofinA
		outfile.write('fi\n')
	print 'File has been catabled, check it out at ./catme.sh'

###########################main

if(not parseArgs()):
	print "Usage: catable.py <file> [options]"
	print "catable takes a file and writes a file (catme.sh) that print the original file to " + wrappedFileName + "."
	print "This is useful if you have access to a remote terminal, but cannot upload a simple file."
	print "Options:"
	print "-m\tWrite file to memory(useful when you can't write to disk on target)"

else:
	infile = open(fileArg,'r');
	outfile = open('catme.sh','w');

	printHeader(outfile)
	#echo wrap file contents
	for line in infile:
		printLine(outfile, escapeString(line))
		
	printFooter(outfile)

