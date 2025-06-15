import calculadora_indices as calc

print("\n--- Cálculo del Índice de Masa Corporal (IMC) ---")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calc.calcular_IMC(peso, altura)
print(f"\nSu IMC es: {round(imc, 2)}")
print("_" * 40)