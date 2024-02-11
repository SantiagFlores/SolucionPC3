class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {', '.join(map(str, self.notas))}")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, *notas):
        self.notas = list(notas)

if __name__ == '__main__':
    try:
        nombre_input = input("Ingrese el nombre del estudiante: ")
        numero_registro_input = input("Ingrese el número de registro del estudiante: ")

        alumno_objeto = Alumno(nombre_input, numero_registro_input)

        edad_input = int(input("Ingrese la edad del estudiante: "))
        alumno_objeto.set_edad(edad_input)

        notas_input = input("Ingrese las notas del estudiante separadas por comas: ")
        notas_lista = list(map(float, notas_input.split(',')))
        alumno_objeto.set_notas(*notas_lista)

        alumno_objeto.display()
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para la edad y las notas.")
    except Exception as e:
        print(f"Error inesperado: {e}.")
