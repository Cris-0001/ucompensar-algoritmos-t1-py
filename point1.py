nValues = int(input("Enter the number of values: "))
accumulate = 0

for i in range(nValues):
    value = int(input("Enter a value: "))
    accumulate += value

print('the sum is: ', str(accumulate))
