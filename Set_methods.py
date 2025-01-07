# Add method is use to add element in set

set = {1,2,3}
set.add(4)
set.add(45)
print(f"Add element in set using add method : {set}\n")

# Update method is use to 2 or more then 2 elements in set

set.update([5,6,7,8,9,10]) # Update elements are written in [ ] brackets
print(f"Set elements after using update method : {set}\n")

# Remove method is use to remove the element from the set

set.remove(3)
set.remove(45)
print(f"Using remove method and removing 3 and 45 from set : {set} ")

# Discard the element from the set but if element not present in it so it doesnt raise any error

Set1 = {1,2,3,4,5}
Set1.discard(2) # this line code will remove the 2 element from the set
Set1.discard(87) # here 87 is not in the set but still no error will occur
print(f"Here using discard method and removing 2 from set : {Set1}")

