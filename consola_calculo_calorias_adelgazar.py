import calculadora_indices as calc

print("\n--- Cálculo de Calorías Recomendadas para Adelgazar ---")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese el valor correspondiente al género (5 si es hombre, -161 si es mujer): "))

mensaje = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(f"\n{mensaje}")
print("_" * 40)