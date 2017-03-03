import math

def is_prime(num): #Function that will determin if a number is prime
	if num == 2 or num == 3: #Checking if the starting value is 2 or 3
		return True #If so return True
	i = 3 #Start the iterator at 3
	if num % 2 == 0: #Checking if the number is divisible by 2
		return False #If so return False
	while i <= math.floor(math.sqrt(num)): #Checking if the iterator is less than the square root of the number being tested
		if num % i == 0: #Checking if the number is divisible by the iterator
			return False #If so return False
		i += 2 #Increment the iterator by 2
	return True #Return true since the number is prime

def get_primes(start): #Function that will produce prime numbers
	i = start #Iterating variable that will start at the provided number
	myArray = [] #Creating a list that will hold prime numbers
	while i <= 2000000: #Will find all prime numbers below 2000000
		if (is_prime(i) == True): #Calling the is_prime function to check if a number is prime
			myArray.append(i) #If so, add it to the list of primes
		i += 1 #Iterate to the next number
	return myArray #Return the list of prime numbers


def sum_primes(primes): #Function that will add all prime numbers produced
	sum = 0 #Start the sum at 0
	for i, val in enumerate(primes): #Iterate throught the list of primes as long as there are elements in the list
		sum += primes[i] #Add the next element to the sum
	print ("summed up the primes bro! Sum = %d" % sum) #Display the sum of the prime numbers

def main(): #Main function that will run the other functions
	print "Please input your starting value" #Prompting the user for a starting input
	strtInt = int(raw_input()) #Converting the input string into a int and storing it
	sum_primes(get_primes(strtInt)) #Calling the functions to find and add prime numbers starting at the provided number


if __name__ == '__main__':
	main() #Run the main function
