import sys

def genTrials(trials, numFirst):
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
            
genTrials(5,4)