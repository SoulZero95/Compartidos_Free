import csv

# Definición de la colección de sectores posibles
sectores = ["Coronel", "Talcahuano", "Lota"]

# Lista para almacenar los pedidos
pedidos = []

# Función para registrar un pedido
def registrar_pedido():
    print("\nRegistro de Pedido")
    id_pedido = input("Ingrese ID del pedido: ")
    nombre_cliente = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    comuna = input("Comuna: ")
    print("Tipos de completos disponibles:")
    print("1. Alemán")
    print("2. A lo pobre")
    print("3. Atómico")
    opcion = int(input("Seleccione tipo de completo (1-3): "))
    while opcion < 1 or opcion > 3:
        print("Opción inválida. Intente nuevamente.")
        opcion = int(input("Seleccione tipo de completo (1-3): "))
    cantidad_aleman = int(input("Cantidad de completos Alemán: "))
    cantidad_lo_pobre = int(input("Cantidad de completos A lo pobre: "))
    cantidad_atomico = int(input("Cantidad de completos Atómico: "))
    
    # Agregar el pedido a la lista
    pedido = {
        "ID": id_pedido,
        "Cliente": nombre_cliente,
        "Dirección": direccion,
        "Comuna": comuna,
        "Alemán": cantidad_aleman,
        "A lo pobre": cantidad_lo_pobre,
        "Atómico": cantidad_atomico
    }
    pedidos.append(pedido)
    print("Pedido registrado correctamente.\n")

# Función para listar todos los pedidos
def listar_pedidos():
    print("\nListado de Pedidos:")
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
    else:
        for pedido in pedidos:
            print(f"ID: {pedido['ID']}\tCliente: {pedido['Cliente']}\tDirección: {pedido['Dirección']}\tComuna: {pedido['Comuna']}\tAlemán: {pedido['Alemán']}\tA lo pobre: {pedido['A lo pobre']}\tAtómico: {pedido['Atómico']}")
    print()

# Función para imprimir hoja de ruta en archivo CSV
def imprimir_hoja_ruta():
    print("\nImprimir Hoja de Ruta")
    print("Sectores disponibles para hoja de ruta:")
    for i, sector in enumerate(sectores):
        print(f"{i+1}. {sector}")
    opcion = int(input("Seleccione el sector para la hoja de ruta (1-3): "))
    while opcion < 1 or opcion > 3:
        print("Opción inválida. Intente nuevamente.")
        opcion = int(input("Seleccione el sector para la hoja de ruta (1-3): "))
    
    sector_seleccionado = sectores[opcion - 1]
    nombre_archivo = f"hoja_ruta_{sector_seleccionado}.csv"
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["ID", "Cliente", "Dirección", "Comuna", "Alemán", "A lo pobre", "Atómico"])
        for pedido in pedidos:
            writer.writerow([pedido["ID"], pedido["Cliente"], pedido["Dirección"], pedido["Comuna"], pedido["Alemán"], pedido["A lo pobre"], pedido["Atómico"]])
    print(f"Se ha generado la hoja de ruta para el sector {sector_seleccionado} en el archivo {nombre_archivo}.\n")

# Función para buscar un pedido por ID
def buscar_pedido_por_id():
    print("\nBuscar Pedido por ID")
    id_buscado = input("Ingrese el ID del pedido a buscar: ")
    encontrado = False
    for pedido in pedidos:
        if pedido["ID"] == id_buscado:
            print(f"Pedido encontrado:")
            print(f"ID: {pedido['ID']}\tCliente: {pedido['Cliente']}\tDirección: {pedido['Dirección']}\tComuna: {pedido['Comuna']}\tAlemán: {pedido['Alemán']}\tA lo pobre: {pedido['A lo pobre']}\tAtómico: {pedido['Atómico']}")
            encontrado = True
            break
    if not encontrado:
        print("Pedido no encontrado.\n")

# Función principal del programa
def main():
    while True:
        print("Bienvenido a El HotDog - Sistema de Pedidos")
        print("1. Registrar Pedido")
        print("2. Listar Pedidos")
        print("3. Imprimir Hoja de Ruta")
        print("4. Buscar Pedido por ID")
        print("5. Salir del Programa")
        
        opcion = int(input("Seleccione una opción (1-5): "))
        while opcion < 1 or opcion > 5:
            print("Opción inválida. Intente nuevamente.")
            opcion = int(input("Seleccione una opción (1-5): "))
        
        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            listar_pedidos()
        elif opcion == 3:
            imprimir_hoja_ruta()
        elif opcion == 4:
            buscar_pedido_por_id()
        elif opcion == 5:
            print("Gracias por utilizar El HotDog - Sistema de Pedidos. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
