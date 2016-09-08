#reading the input
#The minefield will be safed as a 2 dimensional list
width = 0
field = []
f = open("Input-Mines.txt","r")
for idx,line in enumerate(f):
    print(idx)
    if idx ==0:
        width = int(line.split()[0])
        print(width)
        field = [[] for i in range(width)]
    for j,chars in enumerate(line):
        if j == width:    #to cut of the '\n' in the end
            break
        if chars == ' ':
            field[idx-1].append(0)
        else:
             field[idx-1].append(chars)

print(field)
