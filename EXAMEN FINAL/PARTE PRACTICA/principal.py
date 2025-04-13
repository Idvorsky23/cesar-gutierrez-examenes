#EJERCICIO 1 PARTE 2
from modulo_listas import generar_lista, obtener_no_repetidos, ordenar_listas, mayor_par

print("\n--- LLAMANDO FUNCIONES DESDE EL MÓDULO ---")
lista = generar_lista()
no_repetidos = obtener_no_repetidos(lista)
ordenar_listas(no_repetidos)
mayor_par(no_repetidos)