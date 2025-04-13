#EJERCICIO 1 PARTE 1
import random

def generar_lista():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista original: {}".format(lista))
    return lista

def obtener_no_repetidos(lista):
    no_repetidos = list(set(lista))
    print("Lista sin repetidos: {}".format(no_repetidos))
    return no_repetidos

def ordenar_listas(lista):
    descendente = sorted(lista, reverse=True)
    ascendente = sorted(lista)
    print("Orden descendente: {}".format(descendente))
    print("Orden ascendente: {}".format(ascendente))
    return descendente, ascendente

def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    mayor = max(pares) if pares else None
    print("Mayor número par: {}".format(mayor))
    return mayor
