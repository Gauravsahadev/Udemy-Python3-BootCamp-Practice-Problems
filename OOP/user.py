class User:
	pass
	active_user=0
	def __init__(self,first,last,age,likes):
		pass
		self.first=first
		self.last=last
		self.age=age
		self.likes=likes
		User.active_user+=1

	def logout(self):
		pass
		User.active_user-=1
		return "{} is logout.".format(self.first)

	def full_name(self):
		pass
		return "{} {}".format(self.first,self.last)

	def initials(self):
		pass
		return "{}.{}.".format(self.first[0],self.last[0])

	def is_likes(self):
		pass
		return "{} likes {}".format(self.first,self.likes)

	def is_senior(self):
		pass
		return self.age>=65

print(User.active_user)
user1=User("Gaurav","Sahadev",21,"candy")
user2=User("Madhav","Gupta",22,"choc")
print(User.active_user)
print(user2.logout(),user1.logout())
print(User.active_user)

# print(user1.first,user1.last,user1.age)
# print(user2.first,user2.last,user2.age)
# print(user1.full_name())
# print(user2.initials(),user1.initials())

# print(user1.is_likes())
# print(user2.is_senior())

