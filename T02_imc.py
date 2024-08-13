# Escribir un programa que calcule el IMC de una persona, el programa debe solicitar el pesp y la altura (aka datos de entrada)


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

if imc < 18.5:
    print("Estás en la categoría de bajo peso.")
elif 18.5 <= imc < 24.9:
    print("Estás en la categoría de peso normal.")
elif 25 <= imc < 29.9:
    print("Estás en la categoría de sobrepeso.")
else:
    print("Estás en la categoría de obesidad.")