years ={
    "Abir": 2005,
    "Mub": 2006,
    "Mubc": 2007
}

stuff ={ "food":15, "water":25, "energy":100}

# print(stuff["food"])

print(years.items())
print(years.keys())

# print(stuff.popitem())
# print(stuff)

# print(stuff.setdefault("food",66))
# print(stuff)
# print(stuff.setdefault("f2",66))
# print(stuff)

stuff.update(years)
print(stuff)


stuff.update({ "food":1, "water":2, "energy":10})
print(stuff)

print(stuff.get("food"))
