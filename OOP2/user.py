# Program to show the property of getter and setter


class Human:
    pass

    def __init__(self, first, last, age):
        pass
        self.first = first
        self.last = last

        if age >= 0:
            pass
            self._age = age
        else:
            self._age = 0

    def get_age(self):
        pass
        return self._age

    # def set_age(self,new_age):
    # 	pass
    # 	if new_age>=0:
    # 		pass
    # 		self._age=new_age
    # 	else:
    # 		self._age=0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        pass
        if value >= 0:
            pass
            self._age = value
        else:
            raise ValueError("Age can't be negative!")

    @property
    def full_name(self):
        return "{} {} ".format(self.first, self.last)

    @full_name.setter
    def full_name(self, value):
        pass
        self.first, self.last = value.split(" ")


gaurav = Human("gaurav", "sahadev", 21)
# print(gaurav.get_age())
# gaurav.set_age(45)
# print(gaurav.get_age())

print(gaurav.age)
gaurav.age = 45
print(gaurav.age)

print(gaurav.full_name)
gaurav.full_name = "Tim Cooke"
print(gaurav.full_name)
print(gaurav.__dict__)
