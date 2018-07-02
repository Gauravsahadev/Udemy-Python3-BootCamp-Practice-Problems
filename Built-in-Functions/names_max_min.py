names=["Arya","David","Tim","Kevin"]
print(names)
print("MAX=",max(names,key=lambda x: len(x)))
print("Min=",min(names,key=lambda x: len(x)))

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]
print("\n\n",songs)
print(min(songs,key=lambda x:x["playcount"])['title'])
print(max(songs,key=lambda x:x["playcount"])['title'])
