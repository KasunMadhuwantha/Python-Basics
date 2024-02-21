#Dictionaries
band = {
  "vocals": "plant",
  "guitar": "page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items
print(band["vocals"])
print(band.get("guitar"))

#List all keys
print(band.keys())

#list all values
print(band.values())

#list key value pair as tuple
print(band.items())

#verify a key exist
print("guitar" in band)
print("music" in band)

#change values
band["vocals"] = "coverdale"
print(band)

band.update({"bass" : "JPJ"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

#add item
band["drums"] = "bonham"
print(band)

#Delete and clear
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
print(band2)

