def lista(arr):
    print("Productos disponibles:")
    for i in range(len(arr)):
        print(f"{i + 1}. " + arr[i])

productos = []
while True:
    print("\n--------Lista de opciones--------\n1. Agregar un producto\n2. Modificar un producto\n3. Eliminar un producto\n4. Ver todos los productos\n5. Salir")
    opcion = input("Selecciona una opcion: ")
    match opcion:
        case 1:
            while True:
                new = input("\nIngrese un nuevo producto: ")
                if new in productos:
                    print("El producto ya existe")
                else:
                    productos.append(new)
                    break

        case 2:
            lista(productos)
            while True:
                try:
                    prod_index = int(input("Ingrese el índice del producto a modificar:"))-1
                    if prod_index <=0:
                        print("Ingrese un número positivo")
                    else:
                        break
                except:
                    print("Ingrese un índice de la lista")
            new_producto = input("Ingrese el nuevo producto: ")
            productos[prod_index] = new_producto

        case 3:
            lista(productos)
            producto = input("Ingrese el producto a eliminar: ")
            if producto in productos:
                productos.remove(producto)
            else:
                print("El producto no existe")

        case 4:
            lista(productos)

        case 5:
            print("Saliendo...")
            break

        case _:
            print("Opción inválida, intente nuevamente")
