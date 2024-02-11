def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(cal) for cal in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Ingrese solo números enteros separados por comas. Vuelva a intentar.")

if __name__ == '__main__':
    while True:
        try:
            calificaciones = obtener_calificaciones()
            print("Calificaciones ingresadas:", calificaciones)
            break
        except Exception as e:
            print(f"Error inesperado: {e}. Vuelva a intentar.")
