import sys
from random import shuffle

def genTrials(trials, numFirst):
    orig_stdout = sys.stdout
    sys.stdout = open('temp.txt', 'w')
    for i in range(trials):
        for j in range(numFirst):
            sys.stdout.write(str(i+1)),
            sys.stdout.write(",masked"),
            if j%2 == 0:
                sys.stdout.write(",right")
            else:
                sys.stdout.write(",left")
            sys.stdout.write(str("\n"))
        for j in range(12-numFirst):
            sys.stdout.write(str(i+1)),
            sys.stdout.write(",nonmasked"),
            if j%2 == 0:
                sys.stdout.write(",right")
            else:
                sys.stdout.write(",left")
            sys.stdout.write(str("\n"))
    sys.stdout.close()
    sys.stdout=orig_stdout 

    lines = [line.rstrip('\n') for line in open('temp.txt')]
    block1=[]
    block2=[]
    block3=[]
    block4=[]
    block5=[]
    for i in lines:
        if i[0] == "1":
            block1.append(i)
        if i[0] == "2":
            block2.append(i)
        if i[0] == "3":
            block3.append(i)
        if i[0] == "4":
            block4.append(i)
        if i[0] == "5":
            block5.append(i)      
    shuffle(block1)
    shuffle(block2)
    shuffle(block3)
    shuffle(block4)
    shuffle(block5)

    for i in block1:
        print i
    for i in block2:
        print i
    for i in block3:
        print i
    for i in block4:
        print i
    for i in block5:
        print i
        
genTrials(5,8)


