def suma(a, b):
    try:
        resultado = float(a) + float(b)
        return resultado
    except ValueError:
        raise ValueError("Error: Tipo de dato no válido.")

def resta(a, b):
    try:
        resultado = float(a) - float(b)
        return resultado
    except ValueError:
        raise ValueError("Error: Tipo de dato no válido.")

def producto(a, b):
    try:
        resultado = float(a) * float(b)
        return resultado
    except ValueError:
        raise ValueError("Error: Tipo de dato no válido.")

def division(a, b):
    try:
        divisor = float(b)
        if divisor == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        resultado = float(a) / divisor
        return resultado
    except ValueError as e:
        raise ValueError(f"Error: {str(e)}")
import operaciones

def ejecutar_operacion(operacion, num1, num2):
    try:
        resultado = operacion(num1, num2)
        print(f"Resultado de la operación: {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Ejemplo de uso del módulo
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    print("\nOperaciones:")
    ejecutar_operacion(operaciones.suma, num1, num2)
    ejecutar_operacion(operaciones.resta, num1, num2)
    ejecutar_operacion(operaciones.producto, num1, num2)
    ejecutar_operacion(operaciones.division, num1, num2)

