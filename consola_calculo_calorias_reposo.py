import calculadora_indices as calc

print("\n--- Cálculo de Calorías en Reposo (TMB) ---")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese el valor correspondiente al género (5 si es hombre, -161 si es mujer): "))

calorias = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"\nSu tasa metabólica basal es: {round(calorias, 2)} calorías/día")
print("_" * 40)