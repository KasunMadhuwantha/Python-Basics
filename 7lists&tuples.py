users=["Dave","John","Sarah"]
data = ["Dave",42,True]
emptylist = []

print("Dave" in users)

print(users[0])
print(users[-1])
print(users.index("Sarah"))
print(users[0:2])

nums = [4,67,23,5,1]
nums.sort()
print(nums)


#cannot change tuples,only copy list and change
mytuple = tuple(("kasun",2,True))
print(mytuple)