import csv #Importar el modulo csv

def menu():#Crear el menu con la funcion DEF
    print("****Bienvenido al sistema de menu de inventario****")
    print("1.Agregar productos al inventario")#opcion 1 del menu
    print("2.Ver inventario")#opcion 2 del menu
    print("3.Clasificar y exportar productos")#opcion 3 del menu
    print("4.Salir")#opcion 4 del menu
    opcion=input("elija opcion:")#Definir la variable opcion
    return opcion #Devuelve la respuesta

def agregar_productos():#Crear la opcion 1 del menu con la funcion DEF
    id=input("ingrese id del producto:")#Pedir datos al usuario
    nombre=input("ingrese el nombre del producto")#Pedir datos al usuario
    categoria=input("ingrese la categoria[textil,electronica o calzado]")#Pedir datos al usuario con minisculas
    precio=int(input("ingrese el precio del producto"))#Pedir datos al usuario
    with open ("inventario.csv","a", newline="")as inventario:#Abrir el archivo en modo append
        escritor_produc=csv.writer(inventario)#crear la variable para escribir
        escritor_produc.writerow([id,nombre,categoria,precio])#definir la manera en la que se debe escribir en el archivo
    print(f"El producto con id {id} con nombre {nombre}, categorizado como {categoria} fue ingresado con un precio de ${precio}")#Mensaje de que el comando fue ejecutado

def ver_inventario():#Crear la opcion 2 del menu con la funcion DEF
    with open ("inventario.csv", "r", newline="")as inventario:#Abrir el archivo en modo append
        leer_archivo=csv.reader(inventario)
        for row in leer_archivo:
            id, nombre, categoria,precio=row
            print(f"ID: {id}, Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")

    
def clasificar_productos():
    categorias = {
        "electronica": [],
        "textil": [],
        "calzado": []}
    
    # Leer el archivo inventario.csv y clasificar los productos
    with open("inventario.csv", "r", newline="") as inventario:
        leer_archivo = csv.reader(inventario)
        for row in leer_archivo:
            id_producto, nombre, categoria, precio = row
            producto = f"ID: {id_producto}, Nombre: {nombre}, Precio: ${precio}"
            print(f"ID: {id}, Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")

            if categoria.lower() == "electronica":
                categorias["electronica"].append(producto)
            elif categoria.lower() == "textil":
                categorias["textil"].append(producto)
            elif categoria.lower() == "calzado":
                categorias["calzado"].append(producto)
            else:
                print(f"Producto {nombre} con categoría {categoria}  no reconocida.")
    
    # Escribir la clasificación en el archivo clasificacion_productos.txt
    with open("clasificacion_productos.txt", "w") as clasificacion_produc:
        clasificacion_produc.write("----- Productos de Electrónica -----\n")
        for producto in categorias["electronica"]:
            clasificacion_produc.write(f"{producto}\n")
        
        clasificacion_produc.write("\n----- Productos Textiles -----\n")
        for producto in categorias["textil"]:
            clasificacion_produc.write(f"{producto}\n")
        
        clasificacion_produc.write("\n----- Productos de Calzado -----\n")
        for producto in categorias["calzado"]:
            clasificacion_produc.write(f"{producto}\n")
    
    print("Clasificación de productos completada.")


while True:
    opcion = menu() 
    if opcion == '1':
        agregar_productos() 
    elif opcion == '2':
        ver_inventario()     
    elif opcion=="3":
        clasificar_productos()
    elif opcion=="4":
        break
    else:
        print("opcion no valida, por favor ingrese una opcion valida")    