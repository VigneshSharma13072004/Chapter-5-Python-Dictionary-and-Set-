# Write a program in which get 4 friends name and there favrauite books 

D1 = {}
for i in range(5):
    name = input(" \nEnter Friend name : ")
    lang = input(" \nEnter Language name : ")
    D1.update({name : lang})
print(D1)

