class Producto:
    def __init__(self, nombre, codigo, precio, año, marca):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.año = año
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Precio: ${self.precio}")
        print(f"Año: {self.año}")
        print(f"Marca: {self.marca}")
        print("=" * 20)

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_lista(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                producto.mostrar_info()

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No hay productos disponibles para el año {año}.")
        else:
            print(f"Productos para el año {año}:")
            for producto in productos_filtrados:
                producto.mostrar_info()

if __name__ == '__main__':
    catalogo = Catalogo()

    producto1 = Producto("Filtro de Aceite", "FA123", 15.99, 2022, "Bosch")
    producto2 = Producto("Pastillas de Freno", "PF456", 39.99, 2022, "ACDelco")
    producto3 = Producto("Bujía de Encendido", "BE789", 5.49, 2021, "NGK")

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    catalogo.mostrar_lista()

    # Ejemplo de filtrar por año
    catalogo.filtrar_por_año(2022)
