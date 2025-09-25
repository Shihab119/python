info={
  "name":"Shihab",
  "subject":["Math","Science"],
  "age":20
}
print(info)
# mutable(changeable),unordered(no index),key-value pair,dont allow duplicate keys
print(info["name"])
print(info["subject"])
print(info["age"])

info["age"]=21
info["surname"]="Khan"
print(info)


null_dict={}
# dictionary methods
print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
info.update({"city":"Dhaka"})

# sets
# no index,no duplicate values,unordered,sets are mutable(changeable) but the elements inside it are immutable(not changeable)
my_set={1,2,3,4,5}
print(my_set)

collection=set()
collection.add(1)
collection.remove(1)
collection.clear()
collection.pop()

