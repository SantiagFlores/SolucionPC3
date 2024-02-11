import random

def generar_numeros_aleatorios():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista generada:")
    print(lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)

########################################
    import mi_modulosantiago

import mi_modulosantiago

if __name__ == '__main__':
    numeros_aleatorios = mi_modulosantiago.generar_numeros_aleatorios()
    mi_modulosantiago.mostrar_lista(numeros_aleatorios)
    
    mi_modulosantiago.ordenar_y_mostrar(numeros_aleatorios)

