def ZeroPad(hexValue):
    if len(hexValue) == 1:
        hexValue = "0"+hexValue
    return hexValue

def HexRgb(value):
    valueList = list(value)
    #slice array, join values, turn hex to decimal
    r = int("".join(valueList[0:2]),16)
    g = int("".join(valueList[2:4]),16)
    b = int("".join(valueList[4:6]),16)
    print(r,g,b)

def RgbHex(value):
    r = ZeroPad(hex(int(value[0]))[2:])
    g = ZeroPad(hex(int(value[1]))[2:])
    b = ZeroPad(hex(int(value[2]))[2:])
    print(r + g + b)

def Main():
    print("+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")
    rawString = input()
    numberList = rawString.split(" ")
#print(numberList)

    i = 0
    while i < len(numberList):
        if(len(numberList[i]) == 6):
            HexRgb(numberList[i])
            i+=1
            continue
        if(len(numberList[i]) <= 3):
            if(len(numberList[i+1]) <= 3 and len(numberList[i+2]) <= 3):
                decimalArray = [numberList[i],numberList[i+1],numberList[i+2]]
                numberList[i] = decimalArray[:]
                a = i+1
                b = i+3
                RgbHex(numberList[i])
                i+=3

while True:
    Main()


