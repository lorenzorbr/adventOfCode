f = open('data1_1.txt', "r")

count = 0

def getRightNumber(line):
    line = line[::-1]
    for i in range(0, len(line)):
        if((line[i]).isnumeric()):
            return line[i]

def getLeftNumber(line):
    for i in range(0, len(line)):
        if((line[i]).isnumeric()):
            return line[i]

def hasJustOneNumber(line):
    countLine = 0
    for i in range(0, len(line)):
        if((line[i]).isnumeric()):
            countLine += 1

    if countLine == 1:
        return True
    else:
        return False

for i in f.readlines():
    line = i
    print(line)
    if hasJustOneNumber(line):
        number1 = getLeftNumber(line)
        number3 = (int)(number1 + '' + number1)
        count += number3
    else:
        number1 = getLeftNumber(line)
        number2 = getRightNumber(line)
        number3 = (int)(number1 + '' + number2)
        count += number3

print(count)
f.close()