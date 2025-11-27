import uuid

class Usuario:
    def __init__(self, nombre: str, email: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email

    def is_admin(self):
        return False

    def __str__(self):
        return f"Usuario(id={self.id}, nombre={self.nombre}, email={self.email})"

class Cliente(Usuario):
    def __init__(self, nombre: str, email: str, direccion_postal: str):
        super().__init__(nombre, email)
        self.direccion_postal = direccion_postal

    def __str__(self):
        return f"Cliente(id={self.id}, nombre={self.nombre}, email={self.email}, direccion={self.direccion_postal})"

class Administrador(Usuario):
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre, email)

    def is_admin(self):
        return True

    def __str__(self):
        return f"Administrador(id={self.id}, nombre={self.nombre}, email={self.email})"
