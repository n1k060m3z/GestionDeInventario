# models/producto.py

class Producto:
    def __init__(self, nombre, descripcion, precio, stock_inicial, categoria,proveedor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock_inicial
        self.categoria = categoria
        self.proveedor = proveedor

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock para retirar")
        self.stock -= cantidad

    def calcular_valor_total(self):
        return self.stock * self.precio
