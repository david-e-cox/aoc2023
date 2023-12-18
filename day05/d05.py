#!/usr/bin/python3
import re
# Read input file
f=open('input.txt');
#f=open('example.txt')
lines = f.read().splitlines();
f.close()

# Recursive Function, applies maps in order
def applyMap(mapType,inVal,mapData):
    if (mapType=='location'):
        return inVal
    else:
        mapNames = list(mapData.keys())
        for s in mapNames:
            fromMap,toMap = s.split('-to-',1)
            if mapType==fromMap:
                outVal=inVal
                for r in mapData[s]:
                    if inVal >= r[1] and inVal < r[1]+r[2]:
                        outVal = r[0]+inVal-r[1]
                nextMap = toMap
                break
        #print("  {}  {}->{}".format(s,inVal,outVal))
        return applyMap(nextMap,outVal,mapData)

    
# Recursive function, applies maps in reverse order    
def backMap(mapType,inVal,mapData):
    if (mapType=='seed'):
        return inVal
    else:
        mapNames = list(mapData.keys())
        for s in mapNames:
            toMap,fromMap = s.split('-to-',1)
            if mapType==fromMap:
                outVal=inVal
                for r in mapData[s]:
                    if inVal >= r[0] and inVal < r[0]+r[2]:
                        outVal = r[1]+inVal-r[0]
                nextMap = toMap
                break
        #print("  {}-to-{}  {}->{}".format(fromMap,toMap,inVal,outVal))
        return backMap(nextMap,outVal,mapData)


mapData={}
inSection=False

# Seed data is initial stanza in input file
seedData = [int(v) for v in lines[0].split(':')[1].strip().split(' ')]
lines=lines[2:]
lines.append('')  # Need an empty line to close last map 

# Append range info to each section
# Dictionary key has mapping info
for line in lines:
    if len(line)==0:
        mapData[secKey]=mapVals
        inSection=False
        continue
    if not inSection:
        header = line.split(':')[0]
        secKey = header.replace(' map','')
        mapData.update({secKey: [] })
        inSection=True
        mapVals = mapData[secKey];
    else:
        rangeInfo = [int(v) for v in line.strip().split(' ')]
        mapVals.append(rangeInfo)
            

locA=[]
for s in seedData:
    locA.append(applyMap('seed',s,mapData))


# Here we start with a minimum value for a test location
# then run the map backwards and check if the seed is in our range
# If not, increment the location quess and try again

# Quick Start
locTest=27700000
#locTest=-1
done=False
while not done:
    locTest+=1
    if locTest%100000==0:
        print("Location minimum at least {}".format(locTest))
    
    goodSeed = backMap('location',locTest,mapData)
    for j in range(0,len(seedData),2):
        ndx=seedData[j];
        cnt=seedData[j+1];
        if goodSeed>=ndx and goodSeed<ndx+cnt:
            minSeed=goodSeed
            minLoc = locTest
            done = True
            break

print("The answer to Part A is {0:d}".format(min(locA)))
print("The answer to Part B is {0:d}".format(locTest))


