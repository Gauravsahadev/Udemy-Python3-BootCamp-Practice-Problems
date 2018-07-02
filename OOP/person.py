#Program to enter user data using class

class User:
	pass
	def __init__(self,first):
		pass
		self.first=first
		# self.last=last
		# self.age=age

i=1
lst_first=[]
c=[]
while i!=0:
	pass
	user_input=input("Enter the first name: ")
	if user_input=="q":
		break
	else:
		lst_first.append(user_input)
for user in lst_first:
	c.append(User(user))

for v in c:
	print(v.first)

# user1=User("Gaurav","Sahadev",21)
# user2=User("Madhav","Gupta",22)

# print(user1.first,user1.last,user1.age)
# print(user2.first,user2.last,user2.age)