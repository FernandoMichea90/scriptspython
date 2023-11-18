
from mysql.connector import Error

# obtener las consultasa  de productos 
def get_productos(conexion):
    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Definir la consulta SQL
        consulta = """
            SELECT p.codigo as codigo ,p.nombre
            FROM productos p
            WHERE p.activo IN (0, 1)
            AND p.codigo != '00000000ENVIO'
            ORDER BY p.nombre
        """

        # Ejecutar la consulta
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        # devolver listado de productos 
        return resultados
       
    except Error as ex:
        print("Error durante la ejecución de la consulta", ex)

    finally:
        # Cerrar el cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def get_consolidado_bodega(producto,conexion):

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Definir la consulta SQL
        consulta = """
           select cb.cantidad  from consolidado_bodega cb 
            join productos p  on p.id_producto = cb.producto 
            WHERE  p.codigo  = %s
        """
        cursor.execute(consulta, (producto,))
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        # Devolver la cantidad consolidada
        return resultado[0] if resultado else None

    except Error as ex:
        print("Error durante la ejecución de la consulta", ex)

    finally:
        # Cerrar el cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()



def get_consolidado_bodega(producto,conexion):

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Definir la consulta SQL
        consulta = """
           select cb.cantidad  from consolidado_bodega cb 
            join productos p  on p.id_producto = cb.producto 
            WHERE  p.codigo  = %s
        """
        cursor.execute(consulta, (producto,))
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        # Devolver la cantidad consolidada
        return resultado[0] if resultado else None

    except Error as ex:
        print("Error durante la ejecución de la consulta", ex)

    finally:
        # Cerrar el cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()



def get_consolidado_bodega(producto,conexion):

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Definir la consulta SQL
        consulta = """
           select cb.cantidad  from consolidado_bodega cb 
            join productos p  on p.id_producto = cb.producto 
            WHERE  p.codigo  = %s
        """
        cursor.execute(consulta, (producto,))
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        # Devolver la cantidad consolidada
        return resultado[0] if resultado else None

    except Error as ex:
        print("Error durante la ejecución de la consulta", ex)

    finally:
        # Cerrar el cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()


def get_picking(producto,conexion):

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Definir la consulta SQL
        consulta = """
            SELECT SUM(pp.cantidad)  FROM picking p 
            join productos_picking pp  on pp.picking =p.id_picking 
            join productos p2  on pp.producto = p2.id_producto 
            WHERE p.fecha BETWEEN '2023-11-01' AND '2023-11-17'
            and p2.codigo = %s
        """
        cursor.execute(consulta, (producto,))
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        # Devolver la cantidad consolidada
        return resultado[0] if resultado else None

    except Error as ex:
        print("Error durante la ejecución de la consulta", ex)

    finally:
        # Cerrar el cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def get_recepciones(producto,conexion):

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = conexion.cursor()

        # Definir la consulta SQL
        consulta = """
            select SUM(po.cantidad)   from ordenes_compra oc 
            join productos_oc po  on po.orden_compra = oc.id_orden_compra 
            join productos p  on po.producto = p.id_producto 
            where oc.fecha  BETWEEN '2023-11-01' AND '2023-11-17'
            and p.codigo= %s
        """
        cursor.execute(consulta, (producto,))
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        # Devolver la cantidad consolidada
        return resultado[0] if resultado else None

    except Error as ex:
        print("Error durante la ejecución de la consulta", ex)

    finally:
        # Cerrar el cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
