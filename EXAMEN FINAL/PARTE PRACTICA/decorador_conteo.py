#EJERCICIO 2
from datetime import datetime

def conteo(func):
    def wrapper(*args, **kwargs):
        cantidad = len(args) + len(kwargs)
        if cantidad <= 1:
            print("Se necesita más de un parámetro para ejecutar la función.")
            return
        resultado = func(*args, **kwargs)
        print("La función fue ejecutada con {} parámetros.".format(cantidad))
        return resultado
    return wrapper

@conteo
def registrar_estudiante(nombre, edad, nota1, nota2, nota3, nota4):
    now = datetime.now()
    hora = now.hour
    minuto = now.minute
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print("{} de {} años ha sido registrado a las {} horas con {} minutos.".format(nombre, edad, hora, minuto))
    print("Promedio del estudiante: {:.2f}".format(promedio))

registrar_estudiante("Pedro", 30, 15, 18, 17, 16)