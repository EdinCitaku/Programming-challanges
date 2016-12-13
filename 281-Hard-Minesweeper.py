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
                field[idx-1].append('U')
            elif chars == '?':
                field[idx-1].append(chars)
            else:
                 field[idx-1].append(ord(chars)-ord('0'))
                 #field[idx-1].append(chars)
    #sometimes the line ends to early
        while len(field[idx-1])<width and idx!=0:
            field[idx-1].append('U')
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


def sorroundingUnknown(field,x,y):
    "Returns the number of Questionmarks that are sorrounding field[x][y]"
    ret = 0
    for i in range(6):
        if returnAdjacentField(i,len(field),x,y)[0] and (field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]]=='?' or field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]] == 'N'):
            ret+=1
    return ret

#Has a lot of duplicate code with the function above, should think about a prettier solution
def MarkNewmines(field,x,y):
    "Marks all the Mines new found Mines in the field with a 'N'"
    for i in range(6):
        if returnAdjacentField(i,len(field),x,y)[0] and field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]] =='?':
            field[returnAdjacentField(i,len(field),x,y)[1]][returnAdjacentField(i,len(field),x,y)[2]] ='N'

def FindMines(field):
    "Finds all the mines out of a field and returns an array with their coordinates"
    ret = []
    i = 0
    for i,col in enumerate(field):
        for j,el in enumerate(col):
            if el != '?' and isinstance(el,int) and el>0 and el >= sorroundingUnknown(field,i,j):
                 MarkNewmines(field,i,j)


def Markmines(field):
    "Marks all Mines by Setting the 'N' to 'M', also decreases all Numbers around this mine by one"
    ret = 0
    for i, col in enumerate(field):
        for j,el in enumerate(col):
            if(field[i][j] == 'N'):
                field[i][j] =='M'
                ret+=1
                #sets all decreases all sorrounding fields
                for idx in range(6):
                    temp = returnAdjacentField(idx,len(field),i,j)
                    if temp[0] and isinstance(field[temp[1]][temp[2]],int):
                        field[temp[1]][temp[2]] -=1
    return ret

def findimpossibleFields(field):
    "Finds all the 0 in the field and deletes the '?' around them, cause there cant be a mine"
    for i, col in enumerate(field):
        for j,el in enumerate(col):
            if field[i][j] == 0:
                for idx in range(6):
                    temp = returnAdjacentField(idx,len(field),i,j)
                    if temp[0] and field[temp[1]][temp[2]] == "?":
                        field[temp[1]][temp[2]] = "I"


width = 0
f = open("Input-Mines.txt","r")
field = createArray(f)
print(field)
print(field)
#The Solving of the Field takes here place
for i in range(3):
    FindMines(field)
    Markmines(field)
    findimpossibleFields(field)
    print(field)
f.close()
#The output File is written
f2 = open("Output-Mines.txt","w")
for i in range(len(field)):
    for j in range(len(field)):
        if field[i][j] == 'N':
            f2.write(str(i))
            f2.write(str(j))
            f2.write("\n")
print("Abgeschlossen!")
f2.close()
