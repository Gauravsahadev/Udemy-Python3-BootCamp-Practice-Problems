#Import number from 1 to 10
from random import randint

user_num=0
play_again="y"
while play_again!="n":
	rand_num=randint(1,10)
	#Infinite loop starts
	while user_num!=1:

		#Input the number from user
		user_num=int(input("Enter a number from 1 to 10: "))
		#Condition if num is less than user num than print too ,low else num is greater than
		if user_num<rand_num:
			print("the number is too low!") 
		#print too high 
		elif user_num>rand_num:
			print("number is too high!")
		#else print you won the game
		else:
			print("You won the game! \U0001f600 \n")
			user_num=1
	#infinite loop end
#ask user to play again (y/n)
	play_again=str(input("want to play again?(y/n): "))
	if play_again=="y":
		user_num=0
print("Thanks for playing!")	