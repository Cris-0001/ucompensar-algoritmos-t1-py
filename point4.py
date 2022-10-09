nValues = int(input("Enter the number of values: "))
max = 0

for i in range(nValues):
    value = int(input("Enter a value: "))
    max = value if value > max else max

print('the max numer is: ', str(max))
