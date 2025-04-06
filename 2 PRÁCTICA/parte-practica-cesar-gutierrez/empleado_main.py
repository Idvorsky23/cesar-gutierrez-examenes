#1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
class Empleado:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = "Peruana"

    def solicitar_nombre(self):
        print("Nombre del empleado: {}".format(self.nombre))

    def solicitar_edad(self):
        print("Edad del empleado: {} años".format(self.edad))

    def cumpleaños(self):
        self.edad += 1
        print("¡Feliz cumpleaños! Ahora tienes {} años".format(self.edad))

    def aumento_sueldo(self):
        self.sueldo *= 1.3
        print("Sueldo incrementado: S/ {:.2f}".format(self.sueldo))

    def edad_futura(self, año, edad_parametro):
        años_transcurridos = año - 2025
        edad_futura = self.edad + años_transcurridos
        if edad_parametro < self.edad:
            print("No es posible realizar la operación. La edad ingresada es menor a la actual.")
        else:
            print("En el año {} tendrá {} años.".format(año, edad_futura))


# Instanciamos 2 empleados y probamos los métodos
empleado_1 = Empleado("Cesar", 30, 2000)
empleado_2 = Empleado("Karen", 25, 2500)

for emp in [empleado_1, empleado_2]:
    emp.solicitar_nombre()
    emp.solicitar_edad()
    emp.cumpleaños()
    emp.aumento_sueldo()
    emp.edad_futura(2030, emp.edad + 5)
