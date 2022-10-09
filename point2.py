nValues = int(input("Enter the number of values: "))

sum = 0
negative = []
positive = []

for i in range(nValues):
    value = int(input("Enter a value: "))
    if(value < 0):
        negative.append(value)
    else:
        positive.append(value)
    sum += value

print('negative values: ', str(negative) + 'and exist ' + str(len(negative)) + ' negative values')
print('Positive values: ', str(positive) + 'and exist ' + str(len(positive)) + ' positive values')
print('the sum is: ', str(sum))
