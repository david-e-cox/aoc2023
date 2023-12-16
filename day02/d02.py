#!/usr/bin/python3
import collections

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# A copule dictionaries. colors as keys, int values defaulted to zero
colorCount=collections.defaultdict(lambda:0)
pastMax   =collections.defaultdict(lambda:0)

# Constants
limit={'red':12,'green':13,'blue':14}
impossible=set()
powerSum=0
gameSum=0

# Each line in input is the record of a game
for line in lines:
    twoParts =line.split(':')
    gameIndex=int(twoParts[0].split(' ')[1])
    gamesResults = twoParts[1].split(';')
    pastMax.clear()
    for result in gamesResults:
        colorCount.clear()
        # Parse input into color=value dictionary for each cube in this round of a game
        for cube in [ y.split(' ') for y in [x.strip() for x in result.split(',')] ]:
             colorCount[cube[1]] = int(cube[0])

        # Check against limits, declare entire game impossible if limit is broken on a round
        if colorCount['red']>limit['red'] or colorCount['blue']>limit['blue'] or colorCount['green']>limit['green']:
            impossible.add(gameIndex)  # Add this game index to impossible set

        # Create a history of max used (aka min required) for each color during this game
        for clr in limit.keys():
            pastMax[clr]=max(pastMax[clr],colorCount[clr])

    # Calculate power pastMax totals, in this game
    power=1
    for val in pastMax.values():
        power*=val
    #Add to running sum for partB answer
    powerSum+=power

# Calculate totals for Part-A, using impossible set to qualify game 
for g  in range(1,gameIndex+1):
    if g not in impossible:
        gameSum+=g

print("The answer to Part A is {0:d}".format(gameSum))
print("The answer to Part B is {0:d}".format(powerSum))


