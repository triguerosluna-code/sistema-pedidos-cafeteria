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
        


