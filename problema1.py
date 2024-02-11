def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = map(int, fraccion.split('/'))
            if x <= y and y != 0:
                return x, y
            else:
                print("Error: X debe ser menor o igual a Y, y Y no puede ser 0. Vuelva a intentar.")
        except ValueError:
            print("Error: Ingrese números enteros en el formato X/Y. Vuelva a intentar.")
        except ZeroDivisionError:
            print("Error: El denominador (Y) no puede ser cero. Vuelva a intentar.")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100
    porcentaje_redondeado = round(porcentaje)
    if porcentaje_redondeado < 1:
        return 'E'
    elif porcentaje_redondeado > 99:
        return 'F'
    else:
        return f'{porcentaje_redondeado}%'

if __name__ == '__main__':
    while True:
        try:
            x, y = obtener_fraccion()
            resultado = calcular_porcentaje(x, y)
            print(f'Output: {resultado}')
            break
        except Exception as e:
            print(f"Error inesperado: {e}. Vuelva a intentar.")

