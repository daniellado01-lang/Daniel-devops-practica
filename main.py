from models.producto import ProductoElectronico, ProductoRopa
from models.usuario import Cliente, Administrador
from services.Tienda_service import TiendaService


def imprimir_inventario(tienda):
    print("\n=== INVENTARIO ===")
    for p in tienda.listar_productos():
        print(p)


def imprimir_pedidos_cliente(tienda, cliente_id):
    print("\n=== PEDIDOS CLIENTE ===")
    pedidos = tienda.listar_pedidos_usuario(cliente_id)
    if len(pedidos) == 0:
        print("(no hay pedidos)")
    else:
        for p in pedidos:
            print(p)


def imprimir_usuarios(tienda):
    print("\n=== USUARIOS REGISTRADOS ===")
    for usuario in tienda.listar_usuarios():
        print(usuario)


def main():
    tienda = TiendaService()

    # ----- Usuarios -----
    c1 = tienda.registrar_usuario("cliente", "Carlos Ruiz", "carlos@correo.com", direccion_postal="Calle Sol, Sevilla")
    c2 = tienda.registrar_usuario("cliente", "Elena Torres", "elena@correo.com", direccion_postal="Avenida Luna, Bilbao")
    c3 = tienda.registrar_usuario("cliente", "Javier Martín", "javier@correo.com", direccion_postal="Plaza Norte, Zaragoza")
    admin = tienda.registrar_usuario("administrador", "Sofía Admin", "sofia.admin@correo.com")

    imprimir_usuarios(tienda)

    # ----- Productos -----
    p1 = tienda.agregar_producto(ProductoElectronico("Altavoz Bluetooth", 45.50, 40, 18))
    p2 = tienda.agregar_producto(ProductoElectronico("Tablet''", 210.00, 15, 24))
    p3 = tienda.agregar_producto(ProductoRopa("Pantalón", 29.99, 80, "M", "Negro"))
    p4 = tienda.agregar_producto(ProductoRopa("Chaqueta", 59.90, 30, "L", "Verde"))
    p5 = tienda.agregar_producto(ProductoElectronico("Ratón inalámbrico", 25.75, 60, 12))

    imprimir_inventario(tienda)

    # ----- Pedidos -----
    pedido1 = tienda.realizar_pedido(c1.id, [(p5.id, 7), (p1.id, 1)])
    print("\n=== PEDIDO nº1 ===")
    print(pedido1)

    pedido2 = tienda.realizar_pedido(c2.id, [(p3.id, 4), (p2.id, 1), (p1.id, 2)])
    print("\n=== PEDIDO nº2 ===")
    print(pedido2)

    pedido3 = tienda.realizar_pedido(c3.id, [(p4.id, 3), (p2.id, 1)])
    print("\n=== PEDIDO nº3 ===")
    print(pedido3)

    # ----- Inventario después de los pedidos -----
    imprimir_inventario(tienda)

    # ----- Historial de un cliente -----
    imprimir_pedidos_cliente(tienda, c1.id)


if __name__ == "__main__":
    main()
