class Pet:
	pass
	allowed=["dog","cat","rat","fish"]
	def __init__(self,name,species):
		if species not in Pet.allowed:
			raise ValueError("{} is not allowed.".format(species))
		self.name=name
		self.species=species

cat=Pet("kitty","tiger")
print(cat.name,cat.species)