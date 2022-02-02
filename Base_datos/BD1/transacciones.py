import psycopg2 as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s )' # %s es un placeholder
            valores = ('Alex', 'Rojas', 'Alexro@gmail.com')
            cursor.execute(sentencia, valores) # Ejecuta la sentencia con los valores

            sentencia = 'UPDATE persona SET nombre =%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez', 'jcPerez@gmail.com', 1)
            cursor.execute(sentencia, valores) # Ejecuta la sentencia con los valores
except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()
print('Termina la transaccion, se hizo commit')