dict = {
    "Vignesh" : 100,
    "Jeet" : 95,
    "Pinak" : 90,
    "Raw" : 200
}
print(dict)

# Get method is use to get the value of specific key item
print(dict.get("Raw")) # This will give you the value of specific key if the key is not there it will return error

# Item is used to get all pairs of dictionary
print(dict.items()) # Item are stored in a tuple 

# key method is used to display all the key elements 
print(dict.keys())

# Update medthod is use to add or to change the existing pair of dictionary
dict.update({"Raw": 999, "Slaughter":"AURA"})
print(dict)

# Pop is use to diplay the searched element
print(dict.pop("Raw")) # It will pop the value of searched key if the key doesn`t exist so it will show none 
