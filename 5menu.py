title = "menu".upper()
print(title.center(20,"="))
print("coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".")+ "$2".rjust(4))
print("cheesecake".ljust(16,".") + "$12".rjust(4))

first="kasun"
print(title[1:])
print(first.startswith("k"))
print(first.endswith("n"))

#boolian data types
myvalue="True"
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

gpa = "2.64"
import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(2.64))
print(math.floor(2.64))
print(round(2.64))