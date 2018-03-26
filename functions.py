#FUNCTIONS#


def entryroom(finputerror, flocation, ftransitions):
	if finputerror == False:
		print ('\nYou are in {}'.format(flocation[1]))
	
		print ('\nYou can see exits to the following:\n----------')

		for i, t in enumerate(ftransitions[flocation]):
			print ('>', i + 1, t[0])
		print ('----------\n')
	
		print ('Where would you like to go?\n')
