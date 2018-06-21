person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer={l[0]:l[1] for l in person}
print(answer)

#method second
answer2={k:v for k,v in person}
print(answer2)

#method third
answer3=dict(person)
print(answer3)