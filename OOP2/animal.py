# A example of inheritance in OOP


class Animal:
    pass

    def __init__(self, name, species):
        pass
        self.name = name
        self.species = species

    def __repr__(self):
        pass
        return "{} is a {} ".format(self.name, self.species)

    def make_sound(self, sound):
        pass
        print("This animal makes {} ".format(sound))


class Cat(Animal):
    pass

    def __init__(self, name, species, breed, favorite_toy):
        pass
        # Animal.__init__(self,name,species)
        super().__init__(name, species)
        self.breed = breed
        self.favorite_toy = favorite_toy


temp = Cat("kitty", "Cat", "Scotish Fold", "string")
print(temp)
print(temp.species, temp.favorite_toy)


# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy
