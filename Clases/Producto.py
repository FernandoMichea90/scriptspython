# producto.py

class Producto:
    def __init__(self, bodega, ubicacion, codigo, nombre, recepciones, picking, cantidad):
        self.bodega = bodega
        self.ubicacion = ubicacion
        self.codigo = codigo
        self.nombre = nombre
        self.recepciones = recepciones
        self.picking = picking
        self.cantidad = cantidad

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Bodega: {self.bodega}, Ubicación: {self.ubicacion}, Recepciones: {self.recepciones}, Picking: {self.picking}, Cantidad: {self.cantidad}"
