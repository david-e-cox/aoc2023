#!/usr/bin/python3
# to high 8694000
import math
# Read input file
f=open('input.txt');
#f=open('example.txt');
lines = f.read().splitlines();
f.close()

time=lines[0].split(':')[1].strip().split(' ')
dist=lines[1].split(':')[1].strip().split(' ')
time=[int(x) for x in time if len(x)>0] 
dist=[int(x) for x in dist if len(x)>0]

timeB = int(lines[0].split(':')[1].replace(' ',''))
distB = int(lines[1].split(':')[1].replace(' ',''))


count=[]
for i in range(len(time)):
    travel=[]
    for push in range(time[i]):
        travel.append( push*(time[i]-push))
    wins = ([1 for x in travel if x > dist[i]])
    count.append(sum(wins))

#  Certainly there are better ways to do this, but it completes pretty quick
#  Probably should do a bisection search for start/end points of win range
travelB=[]
for push in range(timeB):
    travelB.append( push*(timeB-push))

wins = ([1 for x in travelB if x > distB])
countB=sum(wins)

print("The answer to Part A is {0:d}".format(math.prod(count)))
print("The answer to Part B is {0:d}".format(countB))


