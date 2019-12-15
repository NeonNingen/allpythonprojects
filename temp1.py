temp = 0
totalTemp = 0
numberofTemps = 0
while temp != -100:
    print("Enter the next temperature")
    temp = int(input())
    totalTemp = totalTemp + temp
    numberofTemps = numberofTemps + 1
    averageTemp = totalTemp/numberofTemps
    print(averageTemp)

