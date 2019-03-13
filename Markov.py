from NameGenerator import *


print("****** Baby Name Generator ******")
print("---------------------------------\n")

'''
gender = int(input("Type 0 for Females, 1 for Males:"))
minLen = int(input("Enter the minimum length:"))
maxLen = int(input("Enter the maximum length:"))
order = int(input("Enter the order of the markov model:"))
order = int(input("Enter the number of names to be generated: "))
'''

nameGenerator = NameGenerator()
nameGenerator.generateMap()