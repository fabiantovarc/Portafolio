from Conexion import Conexion
from Usuario import Usuario
from logger_base import log
from CursorDelPool import CursorDelPool

class UsuarioDao:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s, email=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.email, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    usuario1 = Usuario(username='Jorje', password='65424', email='jorjena@mail.com')
    usuario_insertados = UsuarioDao.insertar(usuario1)
    log.debug(f'Usuarios insertados: {usuario_insertados}')

    # Actualizar un registro
    #usuario1 = Usuario(23,'Carlos', 'das4d65as', 'denin@mail.com')
    #usuarios_actualizados = UsuarioDao.actualizar(usuario1)
    #log.debug(f'Usuarios actualizados: {usuarios_actualizados}')

    # Eliminar un registro
    #usuario1 = Usuario(id_usuario=23)
    #usuarios_eliminados = UsuarioDao.eliminar(usuario1)
    #log.debug(f'Usuarios eliminados: {usuarios_eliminados}')

    # Seleccionar objetos
    usuarios = UsuarioDao.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)