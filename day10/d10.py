#!/usr/bin/python3

# Read input file
f=open('input.txt');
#f=open('example4.txt');
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
    if len(nextPt(sumPt(startPt,dir),startPt,map)) > 0:
        startDir=dir
        firstSym=map[sumPt(startPt,dir)[0]][sumPt(startPt,dir)[1]]
        break

if startDir==(0,0):
    printf("FAILURE TO START")
    done=True
else:
    done=False

# Follow path using nextPt until a return to 'S' 
lp =startPt
pt = sumPt(startPt,startDir)
stepLog=[]
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
partA=int(len(stepLog)/2)+1

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(0))


