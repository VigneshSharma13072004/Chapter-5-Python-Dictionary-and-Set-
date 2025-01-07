# Union method for set 
# Here in union method the duplicate elements are repeat once in the set
S1 = {1,2,3,4,5}
S2 = {6,7,8,9,10}
print(f" SET 1 : {S1} \n")
print(f" SET 2 : {S2} \n")

#  Here adding both the set 

result = S1.union(S2)
print(f"Using Union method we get : {result}\n")

# Intersection method is use to display only common elements of two set 

S3 = {1,2,3,4,5}
S4 = {4,5,6,7,8}
print(f" SET 1 : {S3}\n")
print(f" SET 2 : {S4}\n")

# here only displaying the common elements 

result1 = S3.intersection(S4)
print(f"Intersection Method used so get : {result1}\n")

# Difference method used as (-) operater 

S5 = {1,2,3}
S6 = {2,3,4}

diff = S5.difference(S6)
print(f"Using Difference method we got : {diff}\n")