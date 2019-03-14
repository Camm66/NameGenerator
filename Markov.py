from NameGenerator import *


print("\n")
print("****** Baby Name Generator ******")
print("---------------------------------\n")

gender = int(input("Type 0 for Females, 1 for Males:"))
minLen = int(input("Enter the minimum length:"))
maxLen = int(input("Enter the maximum length:"))
number = int(input("Enter the number of names to be generated: "))
print("\n---------------------------------\n")

nameGenerator = NameGenerator()
nameGenerator.generateNames(gender, number, minLen, maxLen)