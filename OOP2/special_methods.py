from copy import copy
class Human:
	pass 
	def __init__(self,first,last,age):
		pass
		self.first=first
		self.last=last
		self.age=age
	def __repr__(self):
		pass
		return "Human named {} {} aged {}".format(self.first,self.last,self.age)
	def __len__(self):
		pass
		return self.age
	def __add__(self,other):
		pass
		if isinstance(other,Human):
			return Human(first="Newborn",last=self.last,age=0)
		return "You can't do that!"
	def __mul__(self,other):
		pass
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "Can't multiply"

j=Human("Jenny","Larsen",22)
k=Human('Kevin','storm',25)
# triplets=j * 3
# triplets[1].first="Jessica"
# print(triplets)

triplets=(j+k)*3
print(triplets)