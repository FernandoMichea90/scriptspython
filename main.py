from consolidado_bodega import get_productos,get_consolidado_bodega,get_picking,get_recepciones
from conexion import conectar_bd
from Clases.Producto import Producto
import json
# Establecer la conexión fuera de la función conectar_bd
conexion = conectar_bd()
# Llamar a la función para ejecutar la consulta
productos = get_productos(conexion)
# Lista para almacenar objetos Producto
productos_lista = []
# Recorrer productos
for producto in productos:
    print(producto)

    # Obtener cantidades consolidadas, picking y recepciones
    cantidad_consolidado_bodega = get_consolidado_bodega(producto[0], conexion)
    print(cantidad_consolidado_bodega)
    cantidad_picking = get_picking(producto[0], conexion)
    print(cantidad_picking)
    cantidad_recepciones = get_recepciones(producto[0], conexion)
    print(cantidad_recepciones)

    # Ajustar cantidades None a cero
    if cantidad_consolidado_bodega is None:
        cantidad_consolidado_bodega = 0
    if cantidad_picking is None:
        cantidad_picking = 0
    if cantidad_recepciones is None:
        cantidad_recepciones = 0

    # Crear instancia de Producto y agregar a la lista
    producto_instancia = Producto(
        bodega="Prueba",  # Puedes ajustar estos valores según tus necesidades
        ubicacion="A-1-1-1-1",
        codigo=producto[0],
        nombre=producto[1],
        recepciones=int(cantidad_recepciones),  # Convertir a entero
        picking=int(cantidad_picking),  # Convertir a entero
        cantidad=int(cantidad_consolidado_bodega)  
    )
    productos_lista.append(producto_instancia)

 #Nombre del archivo JSON
nombre_archivo = "productos.json"

# Convertir la lista de productos a un archivo JSON
with open(nombre_archivo, 'w') as archivo_json:
    json.dump([producto.__dict__ for producto in productos_lista], archivo_json, default=str, indent=2)

print(f"Archivo JSON '{nombre_archivo}' creado correctamente.")