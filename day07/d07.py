#!/usr/bin/python3
import collections

# Read input file
f=open('input.txt');
#f=open('example.txt');
lines = f.read().splitlines();
f.close()

def cardSort(T):
    handRank    = {'fiveOfAKind':7,'fourOfAKind':6,'fullHouse':5,'threeOfAKind':4,'twoPair':3,'onePair':2,'highCard':1}
    cardStrength = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

    # Return tuple with levels of sort, first level is handRank, then cards strength in each position
    return ( handRank[T[0]],
             cardStrength[T[1][0]],
             cardStrength[T[1][1]],
             cardStrength[T[1][2]],
             cardStrength[T[1][3]],
             cardStrength[T[1][4]] )


def cardSort_jacksWild(T):
    handRank    = {'fiveOfAKind':7,'fourOfAKind':6,'fullHouse':5,'threeOfAKind':4,'twoPair':3,'onePair':2,'highCard':1}
    cardStrength = {'A':14,'K':13,'Q':12,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'J':1}
    
    # Return tuple with levels of sort, first level is handRank, then cards strength in each position
    return ( handRank[T[0]],
             cardStrength[T[1][0]],
             cardStrength[T[1][1]],
             cardStrength[T[1][2]],
             cardStrength[T[1][3]],
             cardStrength[T[1][4]] )
             
             

# ---------------------- Part A -------------------------------
T=[]  # Tuple with type,hand,bid
handNdx=0
for line in lines:
    handBid = line.strip().split(' ')
    # Count is dict with number of cards of each kind
    count=collections.Counter(handBid[0])
    # Count Value is list of card-count values
    cntValues=count.values()
    # Ordered logic to set hand type
    if max(cntValues)==5:
        typ='fiveOfAKind'
    elif max(cntValues)==4:
        typ='fourOfAKind'
    elif max(cntValues)==3 and any([True if (x==2) else False for x in cntValues]):
        typ='fullHouse'
    elif max(cntValues)==3:
        typ='threeOfAKind'
    elif sum(bool(x) for x in [True if (x==2) else False for x in cntValues])==2:
        typ='twoPair'
    elif max(cntValues)==2:
        typ='onePair'
    else:
        typ='highCard'

    # Build list with tuples (handType,hand,bid)
    T.append((typ,handBid[0],int(handBid[1])))
    handNdx+=1;

# Sort using function     
Ts = sorted(T,key=cardSort)

# Calculate sum
sumA=0
for i in range(len(Ts)):
    sumA += (i+1)*Ts[i][2]



# ---------------------- Part B -------------------------------
T=[]  # reset type-hand-bid tuple
for line in lines:
    handBid = line.strip().split(' ')
    # Count is dict with number of cards of each kind
    count=collections.Counter(handBid[0])
    # Separate count of wild cards
    wildCards=count['J']
    count['J']=0
    # Count Value is list of card-count values  (excluding Jacks)
    cntValues=count.values()
    
    # Ordered logic to set hand type, now with wildcards
    if max(cntValues)+wildCards==5:
        typ='fiveOfAKind'
    elif max(cntValues)+wildCards==4:
        typ='fourOfAKind'
    elif (  # only need to deal with the zero and one wild card cases
            #   two wild + one pair => four of a kind
            #   three wild + whatever => four/five of a kind
            
            # zero wild: use natural full house logic
            max(cntValues)==3 and any([True if (x==2) else False for x in cntValues])
            or
            #one wild: combine with two-pair logic
            sum(bool(x) for x in [True if (x==2) else False for x in cntValues])==2 and wildCards==1):
        typ='fullHouse'
    elif (max(cntValues)+wildCards)==3:
        typ='threeOfAKind'
    elif (
            # Natural two pair
            sum(bool(x) for x in [True if (x==2) else False for x in cntValues])==2
            or
            # one pair plus wild card
            wildCards==1 and max(cntValues)==2 ):
        typ='twoPair'
    elif (max(cntValues)+wildCards)==2:
        typ='onePair'
    else:
        typ='highCard'

    #print("{}:{}  Natural:{}  Wild:{}".format(handBid[0],typ,count,wildCards))
    T.append((typ,handBid[0],int(handBid[1])))
    handNdx+=1;

# Sort using function     
Ts = sorted(T,key=cardSort_jacksWild)

#Calculate sum
sumB=0
for i in range(len(Ts)):
    sumB += (i+1)*Ts[i][2]

print("The answer to Part A is {0:d}".format(sumA))
print("The answer to Part B is {0:d}".format(sumB))


