from usuarios import mostrar_menu_usuarios
from reportes import mostrar_menu_libros

def Ver_menu_principal():
    while True:
        print("\n")
        print("MENU PRINCIPAL:")
        print("[1] - Mantenedor de usuarios")
        print("[2] - Mantenedor de libros y reportes")
        print("[3] - Salir")
        opcion = input("Ingrese su opcion: ")

        if opcion == '1':
            mostrar_menu_usuarios()
        elif opcion == '2':
            mostrar_menu_libros()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    Ver_menu_principal()
 