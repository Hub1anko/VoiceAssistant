#!/usr/bin/python

DEBUG=True



def empty(text):
	print()

def wersja2(text):
	print(text)

if DEBUG:
	debug=wersja2
else:
	debug=empty

debug("test1")