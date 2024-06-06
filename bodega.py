class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if sum(self.productos.values()) + cantidad <= self.capacidad_maxima:
            if producto in self.productos:
                self.productos[producto] += cantidad
            else:
                self.productos[producto] = cantidad
            return True
        return False

    def retirar_producto(self, producto, cantidad):
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            if self.productos[producto] == 0:
                del self.productos[producto]
            return True
        return False

    def consultar_producto(self, producto):
        return self.productos.get(producto)
