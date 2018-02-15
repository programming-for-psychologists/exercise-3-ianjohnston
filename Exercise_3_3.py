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
        for j in range(6-numFirst):
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
    shuffle(lines)
    for i in lines:
        print i

genTrials(5,4)


