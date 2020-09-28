names = ("Navin","Kiran","Harsh","Navin")
comps = ("Dell","Apple","Ms","Apple")

#zipped = list(zip(names,comps))
#zipped = set(zip(names,comps))
#zipped = dict(zip(names,comps))
zipped = zip(names,comps)
print(zipped)
for (a,b) in zipped:
    print(a,b)