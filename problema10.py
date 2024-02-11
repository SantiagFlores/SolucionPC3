from problema3 import CIRCULO
from problema4 import RECTANGULO

# Resto del código...

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo_objeto = CIRCULO(radio)
    area = circulo_objeto.calcular_area()
    print(f"El área del círculo es: {area}")

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo_objeto = RECTANGULO(largo, ancho)
    area = rectangulo_objeto.calcular_area()
    print(f"El área del rectángulo es: {area}")

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado_objeto = RECTANGULO(lado, lado)  # Un cuadrado es un caso especial de un rectángulo
    area = cuadrado_objeto.calcular_area()
    print(f"El área del cuadrado es: {area}")

if __name__ == '__main__':
    while True:
        print("\nMenu:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada (1-4): ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

