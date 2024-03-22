# Input
C = int(input("Digite el ingreso que desea introducir: "))

# Procesamiento
n = 0
d = 2 * C

while C <= d:
    C = 1.05 * C
    n = n + 1


# Output
print("Los meses que transcurrieron fueron: " + str(n))
print("el capital ganado es de: " + str(C) )