#!/bin/python3

from random import randint
def game(User_input, Computer_Input):
	if User_input==Computer_Input :
		print('Its A Tie Both selected :',User_input)
	elif User_input=='r' and Computer_Input=='p' :
		print('Computer wins, Computer chose:',Computer_Input,' and you chose:',User_input)
	elif User_input=='r' and Computer_Input=='s' :
		print('You win, you chose:',User_input,' and Computer chose:',Computer_Input)
	elif User_input=='s' and Computer_Input=='p' :
		print('You win, you chose:',User_input,' and Computer chose:',Computer_Input)
	elif User_input=='p' and Computer_Input=='r' : 	
		print('You win, you chose:',User_input,' and Computer chose:',Computer_Input)
	elif User_input=='s' and Computer_Input=='r' :
		print('Computer wins, Computer chose:',Computer_Input,' and you chose:',User_input)
	else:
		print('Computer wins, Computer chose:',Computer_Input,' and you chose:',User_input)
Controller=''
while Controller!='q' :
	User=input('''
Lets Play Rock Paper Sicssor
Enter 
r for Rock
p for Paper
s for Scissor
Enter your choice:
''')
	if User!='r' and User!='p' and User!='s' :
		print('Rascal!!! wrong input provided I am not playing Bye Bye')
		exit()
	print('you have chosen:',User)
	Random = randint(1,3)
#print(Computer_input)
	if Random==1 :
		Computer='r'
	elif Random==2 :
		Computer='p'
	else :
		Computer='s'
	print('Computer has chosen:',Computer)
	game(Computer_Input=Computer,User_input=User)
	Controller=input('Press enter key to play "RocK Paper Scissors" again or "q" to quit the game:')
	if Controller!='' and Controller!='q' :	
		print('You did not press "enter" or "q", you are kikcked out _|_')
		exit() 
print('Bye Bye')









