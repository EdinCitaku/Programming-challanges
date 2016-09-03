from PIL import Image
def IterateFunction(z,list):
    #The function we use is set in a text-file called 'Input-Function'
    #The threshold we use is 2
    idx = 0
    while abs(z) < 2:
        w = z   # interim value, so that the power() method can be used properly
        #the function is here applied to the z
        for i in range(0,len(list)-1,2):
            if i == 0:
                z = list[i]*power(w,list[i+1])
            else:
                z = z + list[i]*power(w,list[i+1])
        z = z + list[len(list)-1]*1j
    #    z = z*z -0.221-0.731*1j
        idx+=1
        if(idx > 128):
            break #to save some time
    return idx-1

def power(number,power):
    r = 1
    for i in range(power):
        r = r*number
    return r
#The user is asked what resolution he wants the picture in
print("Hello and welcome to the Trippy-Julia-Fractals-Generator!")
width = int(input("Please enter the width of the picture you want:"))
height = int(input("Please enter the height:"))
#the user can pick his own function
#the txt file has to have the structure xz^n +/- yz^m +/- ... +/- ai
f = open('Input-Function','r')
#the function is safed in the flist in the format [factor,power,factor,power...]
#z^2 + 2z^1 -> [1,2,2,1]
flist = []
factor = 1
#Here the input is put together into the flist
for line in f:
    for word in line.split():
        print(word)
        if word.find("+")!=-1:
            factor = 1
        elif word.find("-")!=-1:
            factor = -1
            print(-1)
        elif word.find("z")!= -1:
            flist.append(float(word[:word.index("z")])*factor)
            flist.append(int(word[word.index("z")+2:]))
        elif word.find("i")!= -1:
            flist.append(float(word[:word.index("i")])*factor)
print(flist)


img = Image.new('RGB',(width,height))

#The Julia Fractals are being generated
for i in range(height):
    for m in(range(width)):
        c = -1 + 2*m/(width-1) + 1j - 2*i/(height-1)*1j
        n = IterateFunction(c,flist)
        img.putpixel((m,i),((255-(255*n)//128,255-(255*n)//128,255-(255*n)//128)))




img.save("fractal2.bmp")
print("The image has been generated!")
