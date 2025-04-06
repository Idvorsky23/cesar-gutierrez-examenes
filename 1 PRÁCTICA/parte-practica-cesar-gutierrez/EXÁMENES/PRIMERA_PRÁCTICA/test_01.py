# Datos del trabajador
nombre = "Cesar"
apellido = "Gutierrez"
salario = 2600.58  # Salario como float
edad = "24"  # Edad en string
compañia = "TSI"

# Conversión de edad a entero
edad_int = int(edad)

# Evaluación del bono según la edad
if edad_int > 30:
    bono_porcentaje = 0.10
    mensaje = "Usted tiene un bono de 10% en el mes de diciembre"
else:
    bono_porcentaje = 0.05
    mensaje = "Usted tiene un bono del 5% en el mes de diciembre"

# Cálculo del bono final: salario^2 + porcentaje de bono
bono_final = (salario ** 2) + (salario * bono_porcentaje)

# Impresión de resultados
print(mensaje)
print("EL BONO FINAL ES:", bono_final)