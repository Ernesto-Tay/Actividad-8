productos = []
while True:
    print("--------Lista de opciones--------\n1. Agregar un producto\n2. Modificar un producto\n3. Eliminar un producto\n4. Ver todos los productos\n5. Salir")
    opcion = input("Selecciona una opcion: ")
    match opcion:
        case 1:
            productos.append(input("Ingrese un producto para añadirlo: "))

        case 2:
            print("Productos disponibles:")
            for i in range(len(productos)):
                print(f"{i+1}. " + productos[i])
            index = int(input("Ingrese el índice del producto a modificar:"))-1
            new_producto = input("Ingrese el nuevo producto: ")
            productos[index] = new_producto

        case 3:
            print("Productos disponibles:")
            for i in range(len(productos)):
                print(f"{i + 1}. " + productos[i])
            producto = int(input("Ingrese el nuevo producto: "))
            if producto in productos:
                productos.remove(producto)
            else:
                print("El producto no existe")

        case 4:
            print("Productos disponibles:")
            for i in range(len(productos)):
                print(f"{i + 1}. " + productos[i])

        case 5:
            print("Saliendo...")
            break

        case _:
            print("Opción inválida, intente nuevamente")
