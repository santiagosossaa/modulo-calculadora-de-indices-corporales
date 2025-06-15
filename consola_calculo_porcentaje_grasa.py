import calculadora_indices as calc

print("\n--- Cálculo del Porcentaje de Grasa Corporal ---")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese el valor correspondiente al género (10.8 si es hombre, 0 si es mujer): "))

porcentaje = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"\nSu porcentaje estimado de grasa corporal es: {round(porcentaje, 2)}%")
print("_" * 40)