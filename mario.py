import cs50

a = 0
reinput = 1
while (reinput):
    print ("Choose a pyramid height: ")
    a = cs50.get_int()
    if (a>=0 and a<24):
        reinput = 0
    else:
        print ("That height is invalid.  Please enter a positive integer between 0 and 23.")

for i in range (1, a+1):
    for n in range (i, a):
        print (" ", end="")

    for m in range (a-i, a):
        print ("#", end ="")

    print ("  ", end="")

    for m in range (a-i, a):
        print ("#", end="")

    print ("")