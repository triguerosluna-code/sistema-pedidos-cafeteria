menu = {
    "cafe con leche": 1500,
    "macha": 2000,
    "smoothie": 2500,
    "pie de manzana": 3500,
    "queque de zanahoria": 3000
}

pedido = []

print("--Bienvenido a la cafeteria --")
nombre_cliente = input("ingrese su nombre aca:")
print(f"Hola {nombre_cliente}, es un gusto atenderle")


while True:
    print("--menu de opciones--")
    print("1. Ver ver el menu de productos")
    print("2. Agregar un producto al pedido")
    print("3. Ver el pedido actual")
    print("4. FInalizar el pedido y salir")
    
    opcion = input("Seleccione una opcion (del 1 al 4): ").strip()
    
    if opcion == "1":
        print("Catalogo de productos:")
        for i, (producto, precio) in enumerate(menu.items(), start=1):
            print(f"{i}. {producto} - ${precio:.2f}")
            print()
            
    elif opcion == "2":
        producto_buscado = input("Ingrese el nombre del producto que desea agregar: ")
        
        for producto, precio in menu.items():
            if producto.lower() == producto_buscado.lower():
                while True:
                    try:
                        cantidad= int(input(f"ingrese la cantidad de {productos}: "))
                        if cantidad > 0:
                            break
                        else: 
                            print("La cantidad debe ser un número entero entero mayor a cero")
                    except ValueError:
                        print("Por favor, ingrese un número entero válido")
                
                pedido.append({
                    "nombre": producto,
                    "precio_unitario": precio,
                    "cantidad": cantidad,
                    "subtotal": precio*cantidad
                })
                print(f"✓ Se agregaron {cantidad} unidad(es) de '{producto}' al pedido.\n")
                break  # <-- Sale del for al encontrar el producto
        else:
            print("❌ El producto ingresado no existe en el menú.\n")
            continue
    
    elif opcion == "3":
        if not pedido: 
            print(" Su pedido actual esta vacio")
            continue
        
        print(f"Pedido actual de {nombre_cliente.upper()}")
        subtotal_parcial = 0.0
        for item in pedido:
            subtotal_parcial += item["subtotal"]
            print(f"-{item["nombre"]} x {item["subtotal"]:.2f}")
        print(f"Subtotal parcial: ${subtotal_parcial:.2f}")
        
    elif opcion == "4"
        if not pedido:
            print("no ha realizado ningun pedido. gracias por visitarno!")
            break
        
        while True:
            try:
                porcentaje_propina = float(input("ingrese el porcentaje de propina que desea dejar: "))
                if 0<= porcentaje_propina <= 100:
                    break
                else:
                    print("El porcentaje debe estar entre 0 y 100.")
            except ValueError:
                print("Por favor ingrese un numero valido.")
                
                        
            

