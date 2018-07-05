class User:
	pass
	active_user=0
	@classmethod
	def display_active_user(cls):
		return "There are currently {} active user".format(cls.active_user)

	@classmethod
	def from_string(cls,data_str):
		pass
		first,last,age=data_str.split(",")
		return cls(first,last,int(age))
	

	def __init__(self,first,last,age,community):
		pass
		self.first=first
		self.last=last
		self.age=age
		self.community=community
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
		return "{} likes {}".format(self.first,self.community)

	def is_senior(self):
		pass
		return self.age>=65

class Moderator(User):
	pass
	total_mods=0
	def __init__(self,first,last,age,community):
		pass
		super().__init__(first,last,age,community)
		Moderator.total_mods+=1

	@classmethod
	def display_active_user(cls):
		pass
		return " There are currently {} active Moderator ".format(cls.total_mods)

temp1=Moderator("gaurav","sahadev",21,"Tech")
temp2=Moderator("gaurav","sahadev",21,"Tech")
temp3=Moderator("gaurav","sahadev",21,"Tech")
temp4=Moderator("gaurav","sahadev",21,"Tech")
temp5=User("gaurav","sahadev",21,"Tech")
print(" ",User.display_active_user(),"\n",Moderator.display_active_user())