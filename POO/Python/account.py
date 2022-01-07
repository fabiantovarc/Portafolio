class Account:
    id       = int
    name     = str
    document = str
    email    = str
    password = str

    def __init__(self, name, document, email, password):        
        self._name      = name
        self._document  = document
        self._email     = email
        self._password  = password


    @property 
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        self._name = name 

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, document):
        self._document = document
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password



    def mostrar_detalles(self):
        print(f"Account [Name: {self._name}, Document: {self._document}, Email:{self._email} ]")
    
    def __str__(self):
        return f"Account [Name: {self._name}, Document: {self._document}, Email:{self._email}, Password: {self._password}]"
    


if __name__ == '__main__':
    Account1 = Account("Andres Herrera", "ANDA876", "Andres@gmail.com", "1234")
    print(Account1)
    #