
nEntero = int(input("Enter the number of pasar a binario: "))

binario = []

while nEntero != 0 :
    newBinario = nEntero % 2
    binario.append(newBinario)
    nEntero = nEntero // 2

print("El resultado en numero binario es: " + str(binario[::-1]))