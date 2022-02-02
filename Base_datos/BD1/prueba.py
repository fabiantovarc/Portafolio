import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE  FROM persona WHERE id_persona IN %s '
            entrada = input('Proporciona el id_persona a eliminar (separados por coma):  ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores) # Ejecuta la sentencia con los valores
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
"""
ELIMINAR MAS DE UN REGISTRO DE LA BASE DE DATOS 
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE  FROM persona WHERE id_persona IN %s '
            entrada = input('Proporciona el id_persona a eliminar (separados por coma):  ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores) # Ejecuta la sentencia con los valores
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
"""

""" UPDATE
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre =%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@gmail.com', 1)
            cursor.execute(sentencia, valores) # Ejecuta la sentencia con los valores
            #conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

"""
"""
se ingresa registros
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s )' # %s es un placeholder
            valores = ('Carlos', 'Lara', 'clara@gmail.com') #se puede agregar una funcion para mostrar los valores y terminos de una persona
            cursor.execute(sentencia, valores) # Ejecuta la sentencia con los valores
            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
"""



"""
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia = 'SELECT * FROM persona WHERE id_persona  =%s' #Si colocamos =%s se puede agregar una variable
            sentencia = 'SELECT * FROM persona WHERE id_persona  IN %s'
            #llaves_primarias = ((1,2,3),)
            #id_persona = input("Proporciona un valor de id_persona: ")
            entrada = input('Proporciona los id\'s a buscar (separado por comas):')
            llaves_primarias = (tuple(entrada.split(',')),)
            #cursor.execute(sentencia, (id_persona,))
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()   #recupera todos los registros
            for registro in registros:
            #registros = cursor.fetchone() 
                print(registro)
            
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
        
        
"""