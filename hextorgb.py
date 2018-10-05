def hextorgb(value):
    valuelist = list(value)
    #slice array, join values, turn hex to decimal
    r = int("".join(valuelist[0:2]),16)
    g = int("".join(valuelist[2:4]),16)
    b = int("".join(valuelist[4:6]),16)
    print(r,g,b)

rawString = input()
numberList = rawString.split(" ")
#print(numberlist)

for i in range(0,len(numberList)):
    hextorgb(numberList[i])
