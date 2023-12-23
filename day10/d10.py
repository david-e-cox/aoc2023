#!/usr/bin/python3
import math

# Read input file
f=open('input.txt');
#f=open('example7.txt');
map = f.read().splitlines();
f.close()

# Create row,col tuples for cardinal directions
N=(-1,0)
E=(0,1)
S=(1,0)
W=(0,-1)

# Create connection dictionary for map elements
con = {'|':[N,S],
       '-':[E,W],
       'L':[N,E],
       'J':[N,W],
       '7':[S,W],
       'F':[S,E]}

def sumPt (pt,delta):
    return (pt[0]+delta[0], pt[1]+delta[1])

def getSym (pt,map):
    return (map[pt[0]][pt[1]])
           
def nextPt (pt,fromPt,map):
    symbol = map[pt[0]][pt[1]]
    if symbol=='.' or symbol=='S':
        return()
    
    for endPt in con[symbol]:
        coor = sumPt(pt,endPt)
        if coor[0]<0 or coor[0]>len(map):
            return ()
        if coor[1]<0 or coor[1]>len(map[0]):
            return()
        #print("  Trying {} using {}".format(coor,endPt))
        if coor != fromPt:
            return coor

# This is really a recursive flood-fill
# From a starting point it regressively adds neighboors for every
# point reachable without crossing path border
def checkPt(pts,outSet,stepLog,map):
    # Base Case
    allIn=True
    for pt in pts:
        if pt not in outSet:
            allIn=False
    if allIn:
        return outSet
    
    nRows=len(map)
    nCols=len(map[0])
    newPts=set()
    cardinal = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]
    for pt in pts:
        cnt=0
        for delta in cardinal:
            np=sumPt(pt,delta)

            if cnt==0 and (np in stepLog):
                break

            if (np[0]<0 or np[0]>=nRows or np[1]<0 or np[1]>=nCols):
                outOfBounds=True
            else:
                outOfBounds=False
                
            if (np not in outSet) and (not outOfBounds):
                if cnt==0:
                    outSet.add(np)
                else:
                    newPts.add(np)
            cnt+=1
    return checkPt(newPts,outSet,stepLog,map)

def showOuts(outSet,stepLog,map,skip):
    nRows=len(map)
    nCols=len(map[0])
    for i in range(int(skip/2),nRows,skip):
        print()
        for j in range(int(skip/2),nCols,skip):
            if (i,j) in outSet:
                print("o",end='')
            elif (i,j) in stepLog:
                print(getSym((i,j),map),end='')
                #print('+',end='')
            else:
                print(".",end='')
            
    print()
        
nRows=len(map)
nCols=len(map[0])

# Find Starting Point
for row in range(nRows):
    for col in range(nCols):
        if map[row][col]=='S':
            startPt=(row,col)
            break

startDir=(0,0)
firstSym='S'
for dir in [N,E,S,W]:
    if   dir==N and getSym(sumPt(startPt,N),map) in ['|','7','F']:
        startDir=dir
    elif dir==E and getSym(sumPt(startPt,E),map) in ['-','7','J']:
        startDir=dir
    elif dir==S and getSym(sumPt(startPt,S),map) in ['|','J','L']:
        startDir=dir
    elif dir==W and getSym(sumPt(startPt,W),map) in ['-','L','F']:
        startDir=dir

if startDir==(0,0):
    printf("FAILURE TO START")
    done=True
else:
    done=False

# Follow path using nextPt until a return to 'S' 
lp =startPt
pt = sumPt(startPt,startDir)
stepLog=[startPt]
while not done:
    np=nextPt(pt,lp,map)
    if len(np)==0:
        # Hit S, or dead end  withouth 2nd connection
        done=True
    else:
        # Keep a log of path coordinates
        stepLog.append(pt)
        lp=pt;
        pt=np;
        #print("Next Symbol is {}, at {}".format(getSym(pt,map),pt))

# distance to mid-point, in steps
partA=int(len(stepLog)/2)


# ------------------------------- Part B Plan A -------------------------------
#14998 is too high
# shoelace algorithm for pseudo code, didn't work...

#area=0
#for i in range(len(stepLog)):
#    j = i+1
#    if j==len(stepLog):
#        j=0
#    area+=stepLog[i][0]*stepLog[j][1]
#    area-=stepLog[i][1]*stepLog[j][0]
#area=abs(area)/2

# ------------------------------- Part B Plan B -------------------------------
## 402 is too low
## 5012 is too high
## 403 is not right

# flood fill with surface normals to select starting points
# This should find localized pockets, works on ALL examples. Also, doesn't work.
#fullSet=set()
#for i in range(nRows):
#    for j in range(nCols):
#        fullSet.add((i,j))
#
#stepSet=set()
#for x in stepLog:
#    stepSet.add(x)
#    
#outSetA=set()
#outSetB=set()
#nRows=len(map)
#nCols=len(map[0])
#
#for i in range(1,len(stepLog)):
#    pt=stepLog[i]
#    normalA = ( -(stepLog[i][1]-stepLog[i-1][1]), (stepLog[i][0]-stepLog[i-1][0]) )
#    normalB = ( +(stepLog[i][1]-stepLog[i-1][1]), -(stepLog[i][0]-stepLog[i-1][0]) )
#    outSetA = checkPt([sumPt(pt,normalA)],outSetA,stepLog,map)
#    outSetB = checkPt([sumPt(pt,normalB)],outSetB,stepLog,map)
#
## Direction of normals is not automatic
## outSet could be interior
## Calculate both
#
#oneSide   = outSetA
#otherSide = outSetB
#
#showOuts(outSetB,fullSet.difference(stepLog).difference(outSetA),stepLog)
#
#print("{},{},{}".format(stepLog[0],stepLog[1],stepLog[2]))
#print("{},{},{}".format(stepLog[-3],stepLog[-2],stepLog[-1]))


# ------------------------------- Part B Plan C -------------------------------
# This is a flood fill on a denser grid
# It put spaces between adjacent pipes for flow
# outside count is based on sparse grid coordinates 

denseStepLog=set()
nRows=len(map)
nCols=len(map[0])

denseMap=[ ['.' for j in range(nCols*3)] for i in range(nRows*3) ]

for i in range(nRows):
    for j in range(nCols):
        if (i,j) in stepLog:
            sym=getSym((i,j),map)
            if sym=='|':
                fillVec=[(-1,0),(0,0),(1,0)]
            elif sym=='-':
                fillVec=[(0,-1),(0,0),(0,1)]
            elif sym=='7':
                fillVec=[(0,-1),(0,0),(1,0)]
            elif sym=='J':
                fillVec=[(-1,0),(0,0),(0,-1)]
            elif sym=='F':
                fillVec=[(1,0),(0,0),(0,1)]
            elif sym=='L':
                fillVec=[(-1,0),(0,0),(0,1)]
            elif sym=='S':
                fillVec=[(-1,0),(0,0),(0,1),(1,0),(0,-1)]
            # Note +1 offset in x,y, center of tile is sparse gridpoint
            for pt in fillVec:
                denseMap[3*i+pt[0]+1][3*j+pt[1]+1]='X'
                denseStepLog.add((3*i+pt[0]+1,3*j+pt[1]+1))

# Initalize                
outSet=set()
# Note:
# Starting point should be generalized using S and outside normal
# Here just taking upper right corner as "outside"
outSet = checkPt([(1,1)],outSet,denseStepLog,denseMap)
showOuts(outSet,denseStepLog,denseMap,3)
cnt=0
for i in range(nRows):
    for j in range(nCols):
        if (3*i+1,3*j+1) in outSet:
            cnt+=1

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {}".format(nRows*nCols-cnt-len(stepLog)))


