# A example of inheritance in OOP


class Animal:
    pass
    cool = True

    def make_sound(self, sound):
        pass
        print("This animal makes {} ".format(sound))


class Cat(Animal):
    pass


temp = Cat()
temp.make_sound("Meow")
print(temp.cool)
