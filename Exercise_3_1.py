def repetition(letters, numberBeforeSwitch, numRepetitions):
    for i in range(numRepetitions):
        for i in letters:
            for j in range(numberBeforeSwitch):
                print i
        

repetition(['A','B'],3,1)

