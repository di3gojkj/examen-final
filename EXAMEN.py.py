# productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]}
# El campo indica el tipo de disco, es decir si es mecánico (DD) o es de estado sólido (SSD)
productos = {"8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
             "2175HD": ["Lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
             "JjFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
             "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
             "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
             "J23FHD": ["Lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
             "342FHD": ["Lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
             "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}

# stock = {modelo: [precio, cantidad]}
stock = {"8475HD": [387990, 10],
         "2175HD": [327990, 4],
         "JjFHD": [424990, 1],
         "fgdxFHD": [664990, 21],
         "J23FHD": [290890, 32],
         "342FHD": [444990, 7],
         "GF75HD": [749990, 2],
         "UWU131HD": [349990, 1],
         "FS1230HD": [249990, 0]
}

def stock_marca():
    marca = input("\nIngrese la marca a consultar: ").strip().upper()
    print(f"\nStock de notebooks marca {marca}:")
    encontrado = False
    
    for codigo, info in productos.items():
        if info[0].upper() == marca: 
            stock_cantidad = stock.get(codigo, [0, 0])[1]
            print(f"Código: {codigo} - Stock: {stock_cantidad}")
            encontrado = True
    
    if not encontrado:
        print(f"No se encontraron productos de la marca {marca}")

def busqueda_precio():
    try:
        precio_min = float(input("Ingrese precio mínimo: "))
        precio_max = float(input("Ingrese precio máximo: "))
        
        print(f"\nProductos en el rango de precio {precio_min} - {precio_max}:")
        productos_encontrados = []
        
        for codigo, info in productos.items():
            if codigo in stock:
                precio = stock[codigo][0]  
                stock_cantidad = stock[codigo][1]  
                
                if precio_min <= precio <= precio_max and stock_cantidad > 0:
                    marca = info[0] 
                    productos_encontrados.append(f"{marca} - {codigo} - Precio: ${precio} - Stock: {stock_cantidad}")
        
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No hay notebooks en ese rango de precios.")
            
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos")

def actualizar_precio():
    modelo = input("Ingrese el código del modelo: ").strip().upper()
    
    if modelo not in productos:
        print("Error: El modelo ingresado no existe")
        return
    
    try:
        precio_nuevo = float(input("Ingrese el nuevo precio: "))
        
        if modelo in stock:
            precio_anterior = stock[modelo][0]
            stock[modelo][0] = precio_nuevo
            print(f"Precio actualizado exitosamente:")           
        else:
            print("Error: El modelo no existe en el stock")
             
    except ValueError:
        print("Error: Debe ingresar un precio válido")


     
    

def mostrar_menu():
    print("\n*** MENU *** ")
    print("1. Stock por marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")

while True:
    mostrar_menu()
    
    try:
        opcion = int(input("Ingrese una opción (1-4): "))
        
        if opcion == 1:
            stock_marca()
        elif opcion == 2:
            busqueda_precio()
        elif opcion == 3:
            actualizar_precio()
        elif opcion == 4:
            print("programa finalizado...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
            
    except ValueError:
        print("Error: Debe ingresar un número válido")
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
        break