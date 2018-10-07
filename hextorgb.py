def HexRgb(value):
    valueList = list(value)
    #slice array, join values, turn hex to decimal
    r = int("".join(valueList[0:2]),16)
    g = int("".join(valueList[2:4]),16)
    b = int("".join(valueList[4:6]),16)
    print(r,g,b)

def RgbHex(value) #argument is array
    r = hex(value[0])
    g = hex(value[1])
    b = hex(value[2])
    print(r + g + b)


rawString = input()
numberList = rawString.split(" ")
#print(numberlist)

for i in range(0,len(numberList)):
    HexRgb(numberList[i])
