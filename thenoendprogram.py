import random

random.seed(10)
secret = round(random.random()*10)

print ("Guess the secret number from 1 - 10!")
val = input("Enter your value: ") 

while int(val) != int(secret):
	print ("Please try again")
	val = input("Enter your value: ") 
	if val == int(secret):
		break
print ("You did it. The secret number is : " + str(secret))


 