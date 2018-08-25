num1 = False
num2 = False
num3 = False
num4 = False

print ("Press 1 for addition")
print ("Press 2 for subtraction")
print ("press 3 for multiplcation")
print ("press 4 for division")
asmd = input ("Enter number here ---> ")

#------------------------------------------------------------------------

if asmd == "1":
    inputadd1 = input ("what is the first number in the equation ---> ")
    inputadd2 = input ("what is the second number in the equation ---> ")
    eql1 =float( inputadd1) +float( inputadd2)
    print (eql1)
    quit ()
#------------------------------------------------------------------------
if asmd == "2":
    inputadd3 = input ("what is the first number in the equation ---> ")
    inputadd4 = input ("what is the second number in the equation ---> ")
    eql2 =float( inputadd3) -float( inputadd4)
    print (eql2)
    quit ()

if asmd == "3":
    inputadd5 = input ("what is the first number in the equation ---> ")
    inputadd6 = input ("what is the second number in the equation ---> ")
    eql3 =float( inputadd5) *float( inputadd6)
    print (eql3)
    quit ()

if asmd == "4":
    inputadd7 = input ("what is the first number in the equation ---> ")
    inputadd8 = input ("what is the second number in the equation ---> ")
    eql4 =float( inputadd7) /float( inputadd8)
    print (eql4)
    quit ()
