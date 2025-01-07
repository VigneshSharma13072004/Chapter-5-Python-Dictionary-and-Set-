# Write a program to form a dictionary of hindi words and there english translation
D1 = {}
for i in range(5):
 key = input("Enter the Hindi word : ")
 value = input("English translation : ")
 D1.update({key : value})
print(f"List of the pairs of hindi and there english translations : {D1}")

