import calculadora_indices as calc

print("\n--- Cálculo de Calorías con Actividad Física ---")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese el valor correspondiente al género (5 si es hombre, -161 si es mujer): "))

print("\\nNiveles de actividad física disponibles:")
print("1.2 → Poco o ningún ejercicio")
print("1.375 → Ejercicio ligero (1-3 días/semana)")
print("1.55 → Ejercicio moderado (3-5 días/semana)")
print("1.72 → Deportista (6-7 días/semana)")
print("1.9 → Atleta (entrenamientos dobles)")

valor_actividad = float(input("Ingrese el valor numérico correspondiente a su actividad física: "))

calorias = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(f"\nCalorías estimadas quemadas por día con actividad física: {round(calorias, 2)}")
print("_" * 40)