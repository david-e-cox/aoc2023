#!/usr/bin/python3

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

rowMax=len(lines[0])
colMax=len(lines)

def adjecentNdx(rowCol,rowMax,colMax):
    # index of all 8 neighbors
    ndx = [ (rowCol[0]-1, rowCol[1]-1),
            (rowCol[0]-1, rowCol[1]),
            (rowCol[0]-1, rowCol[1]+1),
            (rowCol[0],   rowCol[1]-1),
            (rowCol[0],   rowCol[1]+1),
            (rowCol[0]+1, rowCol[1]-1),
            (rowCol[0]+1, rowCol[1]),
            (rowCol[0]+1, rowCol[1]+1)]
    # remove out of bound points
    validNdx=[]
    for pt in ndx:
        if pt[0]>=0 and pt[0]<rowMax and pt[1]>=0 and pt[1]<colMax:
            validNdx.append(pt)
    return validNdx


# Numbers and the properties are tracked by index, in a list
numberList=[]     # List of all numbers in the input
validList=[]      # Indicates if a number is valid part (has nearby symbol)
gearList=[]       # If an element is not empty, has coordinates of the nearby *

# Initialize
rowCnt=0
colCnt=0
validPart=False 
withinNumber=False
nearGear=set()

# Run through the file by lines (aka rows)
for line in lines:
    colCnt=0
    for c in line:
        if c.isdigit():
            withinNumber=True
            # Search a 8 adjacent points
            for pt in adjecentNdx((rowCnt,colCnt),rowMax,colMax):
                a=lines[pt[0]][pt[1]]
                if (not a.isdigit()) and (not a=='.'):
                    # has a symbol adjacent, set as validPart
                    validPart=True
                    # Has a * adjacent add coordinates of * to nearGear variable
                    if a=='*':
                        nearGear.add(pt)
        else:
            if (withinNumber):  # We were in a number, not anymore: collect stats on this number
                if len(nearGear)>1:
                    print("   Warning Double Gear Hit at {},{}:   {}".format(rowCnt,colCnt,nearGear))
                validList.append(validPart)
                gearList.append(nearGear)
                # Reset these for next number
                validPart=False
                nearGear=set()
            withinNumber=False
        colCnt+=1
    # If the last entry in a row is a digit, force end to in-number, register valid status
    if c.isdigit():
        validList.append(validPart)
        gearList.append(nearGear)
        nearGear=set()
    withinNumber=False  # number's can't cross between rows
    rowCnt+=1

# Get a list of all the numbers in the puzzle input
for line in lines:
    numberLine = ''.join(c if c.isdigit() else '.' for c in line)
    num = [ int(n) for n in numberLine.split('.') if len(n)>0 ]
    for n in num:
        numberList.append(n)

#Compute totals         
sumA=0
for i in range(len(numberList)):
    if (validList[i]):
        sumA+=numberList[i]

sumB=0
for i in range(len(gearList)):
    for j in range(i+1,len(gearList)):
        for pt in gearList[i]:
            if pt in gearList[j]:
                sumB+=numberList[i]*numberList[j]

print("The answer to Part A is {0:d}".format(sumA))
print("The answer to Part B is {0:d}".format(sumB))


