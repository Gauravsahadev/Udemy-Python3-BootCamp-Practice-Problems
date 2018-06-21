# Playlist to display songs and overall duration of all songs.

#adding the playlist in dictionary
playlist=dict(title="gaana.com",
	author="gaurav sahadev",
	totalSongs="5",
	songs=[{"title":"Turn it off","artist":"Culture abuse","duration":3.37},
	{"title":"Lovely","artist":"billie eilish","duration":3.50},
	{"title":"Bazaar","artist":"kshmr,marnik","duration":4.00},
	{"title":"Complicated","artist":"kiliara,dmitri vegas,like mike,david guetta","duration":3.57},
	{"title":"Mad love","artist":"david guetta","duration":4.27}])

#printing songs and their artist with duration
print(" Title 			   Artist 			   Duration    ")
for song in playlist["songs"]:
	print(song["title"]+"			",song["artist"]+"				",song["duration"])	

total_duration=0
for song in playlist["songs"]:
	total_duration+=song["duration"]
print("\n\nTotal duration:{}".format(total_duration))