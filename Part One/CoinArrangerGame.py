import sys

coin = 'HHHHHTTTTT' #Starting point for string of coins
turns = 0 #Keep track of turns
remainingTurns = 5 #Variable to display how many turns are left
cSrtEnd = 0 #variable to determine where the initial move is made
dash = True #Boolean that will keep track if there are dashes in the coin pair

while turns < 5: #The loop will run for 5 turns
    dash = True #Keep it at true so that it runs the loop
    while dash :
        print('Select two coins') #Prompting for input
        print(coin) #Printing the coin string
        uIndex = raw_input('') #Storing the user input string
        uIndex = len(uIndex) #Storing the length of the user input
        coinPair = coin[ uIndex : (uIndex + 2)] #Saving the selected coin pair

        if ('-' not in coinPair): #Checking if there is a dash in the selected pair
            dash = False #If so set dash to False

    print('Pair moved:' + coinPair) #Print selected coin pair

    if('--' not in coin): #Making sure no dashes are present to move coin pair to either end of string
        print('Space to where you want to move your pair')
        print(coin)
        cSrtEnd = len(raw_input()) #Getting the input from user
        coin1 = coin[0:uIndex] + '-' #Splitting the coin string and adding dashes in the inner ends
        coin2 = '-' + coin[uIndex + 2:]
        coin = coin1 + coin2 #Reconstructing the string with dashes
        if(cSrtEnd == 0): #If the user chose to place the pair in the beginning
			coin = coinPair + coin #Just add the pair before the coin string
			remainingTurns -= 1 #Decrement the turns
			turns += 1 #Increment the turns
			print ('Turns left: %d' % remainingTurns)

        elif(cSrtEnd == 9): #If user chose to place the pair at the end
			coin = coin + coinPair #Add the pair to the end of the coin string
			remainingTurns -= 1 #Decrement the turns
			turns += 1 #Increment the turns
			print ('Turns left: %d' % remainingTurns)

    else:
        coin = coin.split('--') #Spitting the coin string at the dashes
        coin = coin[0] + coinPair + coin[1] #Adding the pair in between the split string
        coin1 = coin[0:uIndex] + '-' #Adding dashes to where the coin pair previously was
        coin2 = '-' + coin[uIndex + 2:]
        coin = coin1 + coin2 #Reconstructing the updated string

	remainingTurns -= 1 #Decrement the turns
	turns += 1 #Increment the turns
	print ('Turns left: %d' % remainingTurns)

if coin == 'HTHTHTHTHT' or coin == 'THTHTHTHTH': #Checking if the user won
	print 'You Win!'
else:
	print 'Game Over' #User lost
