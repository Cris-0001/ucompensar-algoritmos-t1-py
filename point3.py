nValues = int(input("Enter the number of values: "))

zeros = 0
negative = 0
positive = 0
total = 0


for i in range(nValues):
    value = int(input("Enter a value: "))
    if(value == 0):
        zeros += 1
    elif(value < 0):
        negative += 1
    else:
        positive += 1

    total: int = value

print('percentage of zero numbers: ', str(total * 100 / zeros))
print('percentage of negative numbers: ', str(total * 100 / negative))
print('percentage of positive numbers: ', str(total * 100 / positive))