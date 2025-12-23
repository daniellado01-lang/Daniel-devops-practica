import uuid

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        if precio < 0:
            raise ValueError("El precio no puede tener valores negativos.")
        if stock < 0:
            raise ValueError("El stock no puede tener valores negativos.")
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad: int):
        return cantidad > 0 and self.stock >= cantidad

    def actualizar_stock(self, cantidad: int):
        nuevo_stock = self.stock + cantidad
        if nuevo_stock < 0:
            raise ValueError("Stock insuficiente.")
        self.stock = nuevo_stock

    def __str__(self):
        return f"Producto(id={self.id}, nombre={self.nombre}, precio={self.precio}€, stock={self.stock})"


class ProductoElectronico(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int = 24):
        super().__init__(nombre, precio, stock)
        if garantia_meses <= 0:
            raise ValueError("Garantía inválida.")
        self.garantia_meses = garantia_meses

    def __str__(self):
        return f"ProductoElectronico(id={self.id}, nombre={self.nombre}, precio={self.precio}€, stock={self.stock}, garantia={self.garantia_meses}m)"


class ProductoRopa(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        super().__init__(nombre, precio, stock)
        if not talla or not color:
            raise ValueError("Talla y color son obligatorios.")
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"ProductoRopa(id={self.id}, nombre={self.nombre}, precio={self.precio}€, stock={self.stock}, talla={self.talla}, color={self.color})"
