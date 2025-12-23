import uuid
from datetime import datetime

class PedidoItem:
    def __init__(self, producto_id: str, nombre: str, precio_unitario: float, cantidad: int):
        if cantidad <= 0:
            raise ValueError("Cantidad no válida")
        if precio_unitario < 0:
            raise ValueError("Precio no válido")
        self.producto_id = producto_id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio_unitario * self.cantidad


class Pedido:
    def __init__(self, cliente_id: str, items: list, cliente_nombre: str = None):
        if not items:
            raise ValueError("El pedido debe contener productos")
        self.id = str(uuid.uuid4())
        self.cliente_id = cliente_id
        self.cliente_nombre = cliente_nombre or f"Cliente({cliente_id})"
        self.items = items
        self.fecha = datetime.now()

    def total(self):
        return round(sum(i.subtotal() for i in self.items), 2)

    def __str__(self):
        lineas = "\n".join([f"  - {i.nombre} x{i.cantidad} @ {i.precio_unitario}€ = {i.subtotal()}€" for i in self.items])
        return f"Pedido(id={self.id}, fecha={self.fecha}, cliente={self.cliente_nombre})\n{lineas}\nTotal: {self.total()}€"
