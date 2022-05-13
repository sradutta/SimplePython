# Our Dictionaries
emptydic = {}
stuff = {"food": 15, "energy": 100, "enemies": 3}

# Methods
print(stuff.get("enemies"))
print(stuff.keys())
print(stuff.values())
print(stuff.items())

print(stuff.popitem()) #Remotes the last item of the dictionary
print(stuff)

print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)

new_items = {"rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)
up_new = {"food": 3}
stuff.update(up_new)
print(stuff)
stuff.update(food = 5, cookies = 11)
print(stuff)
