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
else:
    bono_porcentaje = 0.05

bono_final = (salario ** 2) + (salario * bono_porcentaje)

# Crear la lista vacía
datos_trabajador = []

# Agregar los datos a la lista
datos_trabajador.extend([nombre, salario, edad, compañia, bono_final])

# Definir si está trabajando
trabajando = True  # Cambiar a False si ya no trabaja

print("LISTA DE DATOS DE TRABAJADOR:",datos_trabajador)

# Mostrar el tamaño de la lista
print("Tamaño de la lista:", len(datos_trabajador))

# Mensaje si está trabajando o no
if trabajando:
    print(f"El trabajador {nombre} {apellido} se encuentra trabajando actualmente en la compañía.")
else:
    print(f"El trabajador {nombre} {apellido} ya no se encuentra trabajando actualmente en la empresa.")
