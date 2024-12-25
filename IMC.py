#Calculadora de IMC
# Solicitar datos 
Val = True
while Val:
    try:
        
        nombre = input("Ingrese su nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        apellido_paterno = input("Ingrese su apellido paterno: ").strip()
        if not apellido_paterno:
            raise ValueError("El apellido paterno no puede estar vacío.")
        apellido_materno = input("Ingrese su apellido materno: ").strip()
        if not apellido_materno:
            raise ValueError("El apellido materno no puede estar vacío.")
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            raise ValueError("Ingrese una edad válida (entre 0 y 120).")
        altura = float(input("Ingrese su altura (en metros): "))
        if altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        peso = float(input("Ingrese su peso (en kg): "))
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")

        # Cálculo del IMC
        imc = peso / (altura ** 2)
        print(f"IMC: {imc:.2f}")
        
        Val = False
    except ValueError as e:
        print(e)  # Muestra el mensaje de error específico

# Determinar condición según IMC
if imc < 18.5:
    condicion = "Peso bajo"
    recomendacion = "Aumenta tu consumo de calorías saludables y consulta a un nutricionista para mejorar tu peso de forma segura."
elif 18.5 <= imc <= 24.99:
    condicion = "Peso normal"
    recomendacion = "Mantén una dieta equilibrada y realiza actividad física regularmente para conservar tu peso ideal."
elif 25.0 <= imc <= 29.99:
    condicion = "Sobrepeso"
    recomendacion = "Considera una dieta balanceada y aumenta tu actividad física para reducir el peso gradualmente."
elif 30.0 <= imc <= 34.99:
    condicion = "Obesidad leve"
    recomendacion = "Consulta con un especialista en nutrición y realiza actividad física supervisada para evitar complicaciones."
elif 35.0 <= imc <= 39.99:
    condicion = "Obesidad media"
    recomendacion = "Es importante buscar ayuda médica para un plan integral que incluya dieta, ejercicio y asesoramiento médico."
else:  # IMC >= 40
    condicion = "Obesidad mórbida"
    recomendacion = "Busca atención médica inmediata para tratar tu salud y evitar riesgos graves."

# Mostrar resultados
print("\n===== Resultados =====")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Altura: {altura:.2f} m")
print(f"Peso: {peso:.2f} kg")
print(f"IMC: {imc:.2f}")
print(f"Condición: {condicion}")
print(f"Recomendación: {recomendacion}")

