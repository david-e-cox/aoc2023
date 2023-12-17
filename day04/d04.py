#!/usr/bin/python3

# Read input file
#f=open('example.txt');
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Compute score for Part-A rules
def computeScore(win,have):
    winCount=computeWins(win,have)
    if winCount>0:
        score=2**(winCount-1)
    else:
        score=0
    return score

# Computer number of wins on a card
def computeWins(win,have):
    winCount=0
    for n in win:
        if n in have:
            winCount+=1
    return winCount

# Recursive function to update cardCount based on wins along each turn
def addCards(cards, cardCount,turn,lastTurn):
    winCount = computeWins(cards[turn][0],cards[turn][1])
    if turn==lastTurn-1:
        return cardCount
    else:
        for i in range(winCount):
            cardCount[turn+1+i]+=cardCount[turn]
        return addCards(cards,cardCount,turn+1,lastTurn)


# Initialize    
cards=[]      # The card deck with win/have numbers
for line in lines:
    winHave=line.split(':')[1].split('|')
    w = winHave[0].strip().split(' ')
    h = winHave[1].strip().split(' ')
    win =  [int(s) for s in w if len(s)>0]
    have = [int(s) for s in h if len(s)>0]
    # Append win/have numbers into a list of cards
    cards.append([win,have])

# PartA
sumA=0
for card in cards:
    sumA+=computeScore(card[0],card[1])

# Part B
# Initialize, one for each card
cardCount = [1 for c in cards]
# Compute total number of cards in final deck
cardTotals = addCards(cards,cardCount,0,len(cardCount))

# Add totals for partB
sumB=0
for n in cardTotals:
    sumB+=n

print("The answer to Part A is {0:d}".format(sumA))
print("The answer to Part B is {0:d}".format(sumB))


