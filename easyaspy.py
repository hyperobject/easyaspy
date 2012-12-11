import scratch
print('[Easy As Py]')
#Looks
def say(s):
	s = str(s)
	print(s)
#Sensing
def ask(s):
	global answer
	s = str(s)
	answer = raw_input(s)
#Operators
from math import sqrt
def join(a, b):
	a = str(a)
	b = str(b)
	return a + b
def mod(a, b):
	return a % b
def letter_of(num, s):
	s = str(s)
	num = num - 1
	return s[num]
def length_of(s):
	s = str(s)
	return len(s)
#Control
def broadcast(s):
	scratchpy.broadcast(s)
def connect():
	ask('Connect to Scratch using default connection? (Yes or No)')
	answer = answer.lower()
	if answer == 'yes':
		scratchpy = scratch.Scratch(host='localhost')
	elif answer == 'no':
		ask('What IP would you like to connect to?')
		scratchpy = scratch.Scratch(host=answer)
	else:
		print('Response not understood.')
