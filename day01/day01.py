#!/usr/bin/python3
import re

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Function to pull first and last number out as two-digit value
def firstLast(line):
    num=(re.findall('[0-9]+',line))
    if len(num)==1: # single instance
        num.append(num[0])
    return int(num[0][0]+num[-1][-1])


# Initialize solution values
partA=0
partB=0

# Part A
for line in lines:
    partA+=firstLast(line)

#Part B
# Dictionary, numbers with pre/post names to allow overlapping replacements
strDict= {'one'  :'one1one',
          'two'  :'two2two',
          'three':'three3three',
          'four' :'four4four',
          'five' :'five5five',
          'six'  :'six6six',
          'seven':'seven7seven',
          'eight':'eight8eight',
          'nine' :'nine9nine'};

for line in lines:
    # Replace with dictionary values
    for textNum in strDict.keys():
        line=line.replace(textNum,strDict[textNum])
    partB+=firstLast(line)


print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


