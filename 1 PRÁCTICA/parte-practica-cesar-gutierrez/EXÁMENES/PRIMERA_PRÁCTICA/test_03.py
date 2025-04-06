# Datos del trabajador
nombre = "Cesar"
apellido = "Gutierrez"
salario = 2600.58  # Salario como float
edad = "24"  # Edad en string
compañia = "TSI"
trabajando = True

# Conversión de edad a entero
edad_int = int(edad)

# Evaluación del bono según la edad
if edad_int > 30:
    bono_porcentaje = 0.10
else:
    bono_porcentaje = 0.05

bono_final = (salario ** 2) + (salario * bono_porcentaje)

# Lista de datos del trabajador
datos_trabajador = [nombre, salario, edad, compañia, bono_final, trabajando]
#Primera lista de datos del trabajador
print("___________________")
print("Datos del trabajador",datos_trabajador)

# Variable de número de hijos
hijos = 2

# Calcular el bono familiar
if hijos > 0:
    bono_familiar = salario * 0.08
    mensaje_bono_familiar = f"Obtiene el bono familiar el cuál es de: {bono_familiar}"
else:
    bono_familiar = "No cumple para obtener el bono familiar"
    mensaje_bono_familiar = bono_familiar

# Agregar el bono familiar a la lista
datos_trabajador.append(bono_familiar)

# Mostrar la lista actualizada
print("___________________")
print("Lista de datos actualizada:", datos_trabajador)
print("___________________")
print(mensaje_bono_familiar)