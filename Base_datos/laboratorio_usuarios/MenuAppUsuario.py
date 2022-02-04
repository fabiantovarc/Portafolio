from Usuario import Usuario
from UsuarioDao import UsuarioDao
from logger_base import log


class MenuAppUsuario:
    opcion = None
    print(f'Bienvenido al menu')

    while opcion !=5:
        print('Opciones del menu')
        print('1. Lista de usuarios')
        print('2. Insertar usuario')
        print('3. Actulizar usuario')
        print('4. Eliminar usuario')
        print('5. Salir')
        opcion = int(input('Escribe tu opcion: '))
        if opcion == 1:
            usuarios = UsuarioDao.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        elif opcion == 2:
            username_var = str(input('Escribe el username: '))
            password_var = str(input('Escribe el password: '))
            email_var    = str(input('Escribe el email: '))
            usuario = Usuario(username= username_var,password=password_var, email=email_var)
            usuarios_insertados = UsuarioDao.insertar(usuario)
            log.info(f'Usuarios insertados {usuarios_insertados}')   
        elif opcion == 3:
            id_usuario_var =int(input("Escribe el ID: "))
            username_var = str(input('Escribe el username: '))
            password_var = str(input('Escribe el password: '))
            email_var    = str(input('Escribe el email: '))
            usuario = Usuario(id_usuario= id_usuario_var, username= username_var,password=password_var, email=email_var)
            usuarios_actualizados = UsuarioDao.actualizar(usuario)
            log.info(f'Usuarios actualizados {usuarios_actualizados}')
        elif opcion == 4:
            id_usuario_var =int(input("Escribe el ID: "))
            usuario = Usuario(id_usuario= id_usuario_var)
            usuarios_eliminados = UsuarioDao.eliminar(usuario)
            log.info(f'Usuarios eliminados {usuarios_eliminados}')
        elif opcion == 5:
           log.info(('Salimos de la aplicacion...')) 
            


