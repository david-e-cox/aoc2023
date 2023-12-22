#!/usr/bin/python3

import numpy as np
# Read input file
f=open('input.txt');
#f=open('example.txt');
lines = f.read().splitlines();
f.close()


#------------------ Part A -----------------------
sumA=0
for line in lines:
    vals=np.array([int(x.strip()) for x in line.split(' ')])
    history=[np.array(vals)]

    done=False
    while not done:
        # Take gradient, append to history
        g=np.diff(vals)
        history.append(g)
        # If any delta is non-zero, continue
        if np.any(g!=0):
            vals=g;
        else:
            done=True
            
    # Extrapolate
    # Put zero on last line
    history[-1]=np.append(history[-1],0)
    # Put extrap val on each line in turn
    for i in range(len(history)-1,0,-1):
        extrapVal = history[i][-1]+history[i-1][-1]
        newEntry = np.append(history[i-1],extrapVal)
        history[i-1] = newEntry

    # Add last value from first line to total
    sumA+=history[0][-1]

    
    
#------------------ Part B ------------------------
sumB=0    
for line in lines:
    vals=np.array([int(x.strip()) for x in line.split(' ')])
    history=[np.array(vals)]

    done=False
    while not done:
        # Take gradient, append to history
        g=np.diff(vals)
        history.append(g)
        # If any delta is non-zero, continue
        if np.any(g!=0):
            vals=g;
        else:
            done=True
            
    # Extrapolate
    # Put zero in first entry of last line
    history[-1]=np.append(0,history[-1])
    # Put extrap value into each line in turn
    for i in range(len(history)-1,0,-1):
        extrapVal = history[i-1][0]-history[i][0]
        newEntry = np.append(extrapVal,history[i-1])
        history[i-1] = newEntry

    # Add first value from first line to total
    sumB+=history[0][0]

print("The answer to Part A is {0:d}".format(sumA))
print("The answer to Part B is {0:d}".format(sumB))


