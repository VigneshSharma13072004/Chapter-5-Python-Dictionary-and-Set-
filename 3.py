# Write a program to input eight numbers from user and display all unique number once
S1 = set()
for i in range(8):
 n = int(input(f"Enter the number {i+1} : "))
 S1.add(n)
print(f"Here are 8 set Elements : {S1}")

