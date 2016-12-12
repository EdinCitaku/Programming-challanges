#The minefield will be safed as a 2 dimensional list
def  createArray(f):
    "Creates a 2Dimensional Array of a Minefeld from an Inputfile"
    #in this sequence the 2 dimensional field is created
    for idx,line in enumerate(f):
        if idx ==0: #in the first line we will find the length of the array
            width = int(line.split()[0])
            field = [[] for i in range(width)]
        for j,chars in enumerate(line):
            if idx == 0:
                break;
            if chars == '\n':
                break
            elif chars == ' ':
                field[idx-1].append(0)
            elif chars == '?':
                field[idx-1].append(chars)
            else:
                 field[idx-1].append(ord(chars)-ord('0'))
                 #field[idx-1].append(chars)
    #sometimes the line ends to early
        while len(field[idx-1])<width and idx!=0:
            field[idx-1].append(0)
    print(field)
    return field
def returnAdjacentField(number,l,x,y):
    if x > 0:
        if number == 0:
            return [True,x-1,y]
        if y>0 and number == 1:
            return [True,x-1,y-1]
        if y<l-1 and number ==2:
            return [True,x-1,y+1]
    if x < l-1:
        if number == 3:
            return [True,x+1,y]
        if y>0 and number ==4:
            return [True,x+1,y-1]
        if y<l-1 and number ==5 :
            return [True, x+1,y+1]
    if y >0 and number == 6:
        return [True,x,y-1]
    if y <l-1 and (field[x][y+1] == '?' or field[x][y+1] == 'N'):
        return [True,x,y+1]
    return [False,-1,-1]

#Long write, there may be a more efficient solution
def sorroundingUnknown(field,x,y):
    "Returns the number of Questionmarks that are sorrounding field[x][y]"
    print("check")
    ret = 0
    for i in range(6):
        if returnAdjacentField(i,len(field),x,y)[0] and field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]]=='?':
            ret+=1
    return ret

#Has a lot of duplicate code with the function above, should think about a prettier solution
def Markmines(field,x,y):
    print("check")
    for i in range(6):
        if returnAdjacentField(i,len(field),x,y)[0] and field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]] =='?':
            field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]] ='N'

def FindMines(field):
    "Finds all the mines out of a field and returns an array with their coordinates"
    ret = []
    i = 0
    for i,col in enumerate(field):
        for j,el in enumerate(col):
            print(isinstance(el,int))
            if el != '?' and isinstance(el,int) and el>0 and el >= sorroundingUnknown(field,i,j):
                 Markmines(field,i,j)

width = 0
f = open("Input-Mines.txt","r")
field = createArray(f)
FindMines(field)
print(field)
