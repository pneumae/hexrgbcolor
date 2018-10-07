def HexRgb(value):
    valueList = list(value)
    #slice array, join values, turn hex to decimal
    r = int("".join(valueList[0:2]),16)
    g = int("".join(valueList[2:4]),16)
    b = int("".join(valueList[4:6]),16)
    print(r,g,b)

def RgbHex(value):
    r = hex(int(value[0]))[2:]
    g = hex(int(value[1]))[2:]
    b = hex(int(value[2]))[2:]
    print(r + g + b)


rawString = input()
numberList = rawString.split(" ")
#print(numberList)

for i in range(0,len(numberList)-2):
#    print(i)
    if(len(numberList[i]) == 6):
        HexRgb(numberList[i])
        continue
    if(len(numberList[i]) <= 3):
        if(len(numberList[i+1]) <= 3 and len(numberList[i+2]) <= 3):
            decArray = [numberList[i],numberList[i+1],numberList[i+2]]
            numberList[i] = decArray[:]
            a = i+1
            b = i+3
            del numberList[i+1:b]
            RgbHex(numberList[i])

