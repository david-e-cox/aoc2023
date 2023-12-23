#!/usr/bin/python3

# Read input file
f=open('input.txt')
#f=open('example.txt')
lines = f.read().splitlines()
f.close()

# Show map utility
def showMap(map):
    for row in map:
        print()
        for c in row:
            print("{}".format(c),end='')

# Manhattan distance            
def calcDist(pt1,pt2):
    return( (abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])) )


# ---------------- Part A ----------------------
#Expand Universe

#Initialize
rowSum=[0 for x in lines]
colSum=[0 for x in lines[0]]

# Get row's and col's to be expanded
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=='#':
            rowSum[i]+=1
            colSum[j]+=1

# Add new columns with copy into new map variable            
starMap =[ [] for x in lines]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        starMap[i].append(lines[i][j])
        if colSum[j]==0:
            starMap[i].append('.')

# Add rows with insert
cnt=0
for i in range(len(lines)):
    cnt+=1
    if rowSum[i]==0:
        starMap.insert(cnt,['.' for x in starMap[i]])
        cnt+=1

# Generate list of stars, with coordinates
starList=[]        
for i in range(len(starMap)):
    for j in range(len(starMap[0])):
        if starMap[i][j]=='#':
            starList.append((i,j))

# Find distance between all stars
dist=[]
for i in range(len(starList)):
    for j in range(i):
        dist.append(calcDist(starList[i],starList[j]))


        
# ------------  Part B -----------------
# Generate list of coordinates of stars
rawStarList=[]        
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j]=='#':
            rawStarList.append((i,j))

# Apply expansion to coordinates, capturing cumlative shifts
expStarList=[]
for loc in rawStarList:
    newRow=loc[0]
    newCol=loc[1]
    for i in range(len(colSum)):
        if (colSum[i]==0) and (loc[1] > i):
            newCol += 999999
    for i in range(len(rowSum)):
        if (rowSum[i]==0) and (loc[0] > i):
            newRow += 999999
    expStarList.append((newRow,newCol))

# Calcuate distance between all stars
distB=[]
for i in range(len(starList)):
    for j in range(i):
        distB.append(calcDist(expStarList[i],expStarList[j]))

print("The answer to Part A is {0:d}".format(sum(dist)))
print("The answer to Part B is {0:d}".format(sum(distB)))


