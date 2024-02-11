import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

if __name__ == '__main__':
    try:
        radio_input = float(input("Ingrese el radio del círculo: "))
        circulo_objeto = CIRCULO(radio_input)
        area_calculada = circulo_objeto.calcular_area()
        print(f"El área del círculo con radio {radio_input} es: {area_calculada}")
    except ValueError:
        print("Error: Ingrese un número válido para el radio del círculo.")
    except Exception as e:
        print(f"Error inesperado: {e}.")

