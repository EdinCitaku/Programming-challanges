def listOfCoins(left,right): #left and right must have the same size
    re = []
    for i in range(len(left)) :
        for char in left[i]:
            if char not in re:
                re.append(char)
        for char in right[i]:
            if char not in re:
                re.append(char)
    return re

f = open('Input','r')
i = 0
left= []
right=[]
weight =[]
for line in f:
    for idx,word in enumerate(line.split()):
        if idx%3 ==0:
            left.append(word)
        elif idx%3 ==1:
            right.append(word)
        else:
            weight.append(word)
coins = listOfCoins(left,right)
#Here the weights will be safed we assume, that only one coin is fake
#Fake coins are lighterdd
#first the program safes the coins, that definitely weight the same
equal = []
numberLeft = [[0 for j in range(len(coins))] for i in range(len(left))]
numberRight = [[0 for j in range(len(coins))] for i in range(len(left))]
#numberLeft and numberRight show how many coins of a type were on one side
for i in range(len(left)):
    for char in left[i]:
        numberLeft[i][coins.index(char)]+=1
    for char  in right[i]:
        numberRight[i][coins.index(char)]+=1

#Here the coins are collected, that definitely have the right weight
for i in range(len(numberLeft)):
    for j in range(len(numberLeft[i])):
        if weight[i] == 'equal' and numberLeft[i][j] is not numberRight[i][j] and coins[j] not in equal:
            equal.append(coins[j])
        elif weight[i] != 'equal' and numberLeft[i][j] is numberRight[i][j] and coins[j]  not in equal and numberLeft[i][j] is not 0:
            equal.append(coins[j])


#The coin, who is not in equal, has the wrong weight
#If there are more weights
notequal = []
for i in range(len(coins)):
    if coins[i]  not in equal:
        notequal.append(coins[i])

#It must be made sure, that the data is consistent
consistent = True
for i in range(len(weight)):
    if(len(notequal))==0:
        break
    if  len(notequal) > 1:
        consistent = False
        break
    if weight[i] == 'equal' and numberLeft[i][coins.index(notequal[0])] != numberRight[i][coins.index(notequal[0])] and numberLeft[i][coins.index(notequal[0])]!=0 :
        consistent = False
        break
    #If there are more than one fake coins its inconsistent regardless -> Only notequal[0] is controlled
    if weight[i]=='left' and numberLeft[i][coins.index(notequal[0])] >=  numberRight[i][coins.index(notequal[0])]:
        consistent = False
        break
    if weight[i]=='right' and numberLeft[i][coins.index(notequal[0])] <=  numberRight[i][coins.index(notequal[0])]:
        consistent = False
        break

#the answer is printed out
if not consistent:
    print("data is incosistent")
elif len(notequal) == 1:
    print(notequal[0]+" is lighter")
else:
    print("no fake coins detected")


#print(coins)
#print(numberLeft)
#print(numberRight)
#print(weight)
#print(equal)
