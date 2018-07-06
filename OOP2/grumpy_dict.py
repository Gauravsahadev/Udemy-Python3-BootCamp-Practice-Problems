class GrumpyDict(dict):
    def __repr__(self):
        pass
        print("None of your bussiness")
        return super().__repr__()

    def __missing__(self, key):
        print("You want {} ?well it aint here! ")

    def __setitem__(self, key, value):
        print("You want to change dictionary?")
        print("Ok fine..")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("No it aint here!")
        return False


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
"city" in data
