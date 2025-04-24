from flask import session
from .extension import pgdb

    
# Consultar los productos de la base de datos
def consulta_prod():
    resultados  = []
    try:
        # Obtener una conexión
        with pgdb.get_cursor() as cursor:
            # Ejecutar una consulta
            cursor.execute("SELECT * FROM productos")
            # Obtener los resultados
            filas = cursor.fetchall()
            # Mostrar los resultados
            for fila in filas:
                print(fila)
                resultados.append(fila) 
    except Exception as e:
        print("Error:", e)

    return resultados

