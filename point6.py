iter = 0
colectionNotes = []
finalNote = 0

while iter == 0 :
    nota = int(input("Ingrese su nota: "))
    if nota == 999:
        break
    if nota < 0  or nota > 100 :
        print("La nota es de 0 a 100, ingrese nuevamente un valor en ese rango")
    else:
        colectionNotes.append(nota)
    print(colectionNotes)

for i in range(len(colectionNotes)):
    finalNote += colectionNotes[i]

print("La nota final es: " + str((finalNote / len(colectionNotes))/10))