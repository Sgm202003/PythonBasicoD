peso = input("Indica tu peso -kg-")
estatura = input("Indica tu estatura en metros -m-")
# Para calcular el indice de masa corporal -IMC- se divide el peso por el resultado de elevar la altura al cuadrado.
imc = round(float(peso)/float(estatura)**2)
print("Tu Indice de Masa Corporal es " + str(imc))