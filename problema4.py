class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

if __name__ == '__main__':
    try:
        largo_input = float(input("Ingrese el largo del rectángulo: "))
        ancho_input = float(input("Ingrese el ancho del rectángulo: "))
        
        rectangulo_objeto = RECTANGULO(largo_input, ancho_input)
        area_calculada = rectangulo_objeto.calcular_area()
        
        print(f"El área del rectángulo con largo {largo_input} y ancho {ancho_input} es: {area_calculada}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para el largo y el ancho del rectángulo.")
    except Exception as e:
        print(f"Error inesperado: {e}.")
