#!/usr/bin/python3
import numpy

# Read input file
f=open('input.txt');
#f=open('exampleB.txt');
mov = f.readline().strip()
f.readline()
lines = f.read().splitlines();
f.close()

posPath=dict()
for line in lines:
    pos=(line.split('=')[0].strip())
    tmp = line.split('=')[1].strip().replace('(','').replace(')','').split(',')
    path=(tmp[0].strip(),tmp[1].strip())
    posPath.update({pos:path})


# ----------------- Part A -----------------------------
## Initialize    
pt='AAA'
movCount=0
done=False
# Walk the map
while not done:
    c=mov[movCount%len(mov)]
    movCount+=1
    if c=='L':
        selNdx=0
    else:
        selNdx=1
    pt = posPath[pt][selNdx]
    if pt=='ZZZ':
        done=True
partA=movCount


# ----------------- Part B -----------------------------
# Initialize    
pts=[x for x in posPath.keys() if x[2]=='A']
repeatAt=[0 for x in pts]
movCount=0
done=False

# Walk the multiple paths
while not done:
    c=mov[movCount%len(mov)]
    movCount+=1
    if c=='L':
        selNdx=0
    else:
        selNdx=1
    nextPts=[]

    # For each path
    for i in range(len(pts)):
        pt=pts[i]
        if posPath[pt][selNdx][2]=='Z':
            # Store the movCount at which we hit a last char Z for this path
            # The path we are taking will repeat every movCount steps
            # Don't overwrite an existing (and smaller) count
            if repeatAt[i]==0:
                repeatAt[i]=movCount
        # Update pts on each simultaneous path
        pts[i] = posPath[pt][selNdx]

    # If we have repeated along every path, then we are done
    if min(repeatAt)>0:
        done=True

# Find least common multiple amoung repeat counts
# That's the point when all paths will hit Z at once
partB=numpy.lcm.reduce(repeatAt)

print("The answer to Part A is {0:d}".format(partA))
print("The answer to Part B is {0:d}".format(partB))


