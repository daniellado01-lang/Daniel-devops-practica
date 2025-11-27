from models.producto import Producto, ProductoElectronico, ProductoRopa
from models.usuario import Usuario, Cliente, Administrador
from models.pedido import Pedido, PedidoItem

class TiendaService:
    def __init__(self):
        self.usuarios = {}
        self.productos = {}
        self.pedidos = {}
        self.email_index = {}

    def registrar_usuario(self, tipo: str, nombre: str, email: str, **kwargs):
        if tipo == "cliente":
            usuario = Cliente(nombre, email, kwargs.get("direccion_postal", ""))
        elif tipo == "administrador":
            usuario = Administrador(nombre, email)
        else:
            raise ValueError("Tipo inválido")
        if email in self.email_index:
            raise ValueError("Email ya existente")
        self.usuarios[usuario.id] = usuario
        self.email_index[email] = usuario.id
        return usuario

    def agregar_producto(self, producto: Producto):
        if producto.id in self.productos:
            raise ValueError("Producto ya existente")
        self.productos[producto.id] = producto
        return producto

    def eliminar_producto(self, producto_id: str):
        if producto_id not in self.productos:
            raise KeyError("Producto no encontrado")
        del self.productos[producto_id]

    def listar_productos(self):
        return list(self.productos.values())

    def obtener_producto(self, producto_id: str):
        if producto_id not in self.productos:
            raise KeyError("Producto no encontrado")
        return self.productos[producto_id]

    def realizar_pedido(self, cliente_id: str, items: list):
        if cliente_id not in self.usuarios:
            raise ValueError("Cliente no existente")
        cliente = self.usuarios[cliente_id]
        if not isinstance(cliente, Cliente):
            raise ValueError("Solo clientes pueden realizar pedidos")
        if not items:
            raise ValueError("El pedido debe contener productos")

        lineas = []
        for pid, cantidad in items:
            producto = self.obtener_producto(pid)
            if not producto.hay_stock(cantidad):
                raise ValueError(f"Stock insuficiente para {producto.nombre}")
            lineas.append(PedidoItem(pid, producto.nombre, producto.precio, cantidad))

        for pid, cantidad in items:
            self.productos[pid].actualizar_stock(-cantidad)

        pedido = Pedido(cliente_id, lineas, cliente.nombre)
        self.pedidos[pedido.id] = pedido
        return pedido

    def listar_pedidos_usuario(self, cliente_id: str):
        return sorted([p for p in self.pedidos.values() if p.cliente_id == cliente_id], key=lambda p: p.fecha)

    def listar_usuarios(self):
        return list(self.usuarios.values())
