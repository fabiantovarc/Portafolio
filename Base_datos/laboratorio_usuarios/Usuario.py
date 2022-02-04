from logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None, email=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
        self._email = email

    def __str__(self):
        return f'''
            ID Usuario: {self._id_usuario}, Nombre: {self._username},
            Contraseña: {self._password}, Email: {self._email}
        '''

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_persona(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return  self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    
if __name__ == '__main__':
    usuario1 = Usuario(username='Fabian',password= '456',email= 'fabian@gmail.com')
    log.debug(usuario1)    

            
        