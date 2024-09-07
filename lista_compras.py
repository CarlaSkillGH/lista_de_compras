# Inicialización de la lista de compras
lista_compras = []

def mostrar_menu():
# Menú que se le mostrará al cliente
    print("Este es nuestro menú, por favor ingresar una opción válida")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

def agregar_articulo():
#Se le solicita al usuario que introduzca el nombre del artículo
    articulo = input("Introduce el nombre del artículo: ")
    lista_compras.append(articulo)
    print(f"'{articulo}' ha sido agregado a la lista.")

def eliminar_articulo():
#En esta opción el usuario podría eliminar un artículo de la lista
    if not lista_compras:
        print("La lista está vacía.")
        return
    
    mostrar_lista()
    try:
        indice = int(input("Introduce el número del artículo a eliminar: "))
        if 0 <= indice < len(lista_compras):
            eliminado = lista_compras.pop(indice)
            print(f"'{eliminado}' ha sido eliminado de la lista.")
        else:
            print("No tenemos ese producto en la lista.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")

def mostrar_lista():
#Este bloque de código imprime los artículos ingresados hasta el momento
    if not lista_compras:
        print("La lista está vacía.")
    else:
        print("Lista de compras:")
        for i, articulo in enumerate(lista_compras):
            print(f"{i}. {articulo}")

def main():
#Función que ejecuta el programa1
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_articulo()
        elif opcion == '2':
            eliminar_articulo()
        elif opcion == '3':
            mostrar_lista()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
    # ¡Código listo para usar!
