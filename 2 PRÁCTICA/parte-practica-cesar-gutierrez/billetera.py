#3. Escribir un programa para gestionar una billetera electrónica (3 ptos):
class BilleteraElectronica:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.soles = saldo_soles
        self.dolares = saldo_dolares
        self.tipo_cambio = 3.80

    def mostrar_saldos(self):
        print("Usuario:", self.nombre, self.apellido)
        print("Saldo en soles: S/ {:.2f}".format(self.soles))
        print("Saldo en dólares: $ {:.2f}".format(self.dolares))

    def transferir(self, de, monto):
        if de.lower() == 'soles':
            if self.soles >= monto:
                self.soles -= monto
                self.dolares += monto / self.tipo_cambio
                print("Transferencia realizada de S/ {:.2f} a dólares.".format(monto))
            else:
                print("Fondos insuficientes en soles.")
        elif de.lower() == 'dolares':
            if self.dolares >= monto:
                self.dolares -= monto
                self.soles += monto * self.tipo_cambio
                print("Transferencia realizada de $ {:.2f} a soles.".format(monto))
            else:
                print("Fondos insuficientes en dólares.")
        else:
            print("Moneda inválida. Usa 'soles' o 'dolares'.")

    def retirar(self, moneda, monto):
        if moneda.lower() == 'soles':
            if self.soles >= monto:
                self.soles -= monto
                print("Retiro exitoso de S/ {:.2f}".format(monto))
            else:
                print("Saldo insuficiente en soles.")
        elif moneda.lower() == 'dolares':
            if self.dolares >= monto:
                self.dolares -= monto
                print("Retiro exitoso de $ {:.2f}".format(monto))
            else:
                print("Saldo insuficiente en dólares.")
        else:
            print("Moneda inválida.")
        self.mostrar_saldos()

billetera = BilleteraElectronica("Cesar", "Gutierrez", 1000, 200)
print(">>> Saldos iniciales:")
billetera.mostrar_saldos()
print("\n>>> Transferencia 1 (de soles a dólares):")
billetera.transferir("soles", 380)
print("\n>>> Transferencia 2 (de dólares a soles):")
billetera.transferir("dolares", 50)
print("\n>>> Transferencia 3 (saldo insuficiente en dólares):")
billetera.transferir("dolares", 1000)
print("\n>>> Retiro en soles:")
billetera.retirar("soles", 200)
print("\n>>> Retiro fallido en dólares:")
billetera.retirar("dolares", 1000)

