def bienvenida():
    print("*****************************************")
    print("*   Bienvenido al Programa de Conversión *")
    print("*              de Temperatura            *")
    print("*     Departamento de Química - EPN      *")
    print("*****************************************")
    print("Por favor, inicie sesión para continuar.")
def sesion():
    # Usuario y contraseña correctos
    usuario = "Admin"
    contraseña = "Secret*"

    # Pedir que ingrese los datos
    usuario_ingresado = input("Usuario: ")
    contraseña_ingresada = input("Contraseña: ")

    # Validación de datos
    while usuario_ingresado != usuario or contraseña_ingresada != contraseña:
        print("Usuario o contraseña incorrectos. Por favor, intente de nuevo.")
        usuario_ingresado = input("Usuario: ")
        contraseña_ingresada = input("Contraseña: ")

    print("Inicio de sesión exitoso.")
def menu():
    print("\nMenú de opciones:")
    print("1. Convertir grados centígrados a grados Fahrenheit.")
    print("2. Convertir grados kelvins a grados centígrados.")
    print("3. Salir del programa.")
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15
def main():
    bienvenida()
    sesion()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            celsius = float(input("Ingrese la temperatura en grados centígrados: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados centígrados son {fahrenheit} grados Fahrenheit.")
        elif opcion == "2":
            kelvin = float(input("Ingrese la temperatura en kelvins: "))
            celsius = kelvin_a_celsius(kelvin)
            print(f"{kelvin} kelvins son {celsius} grados centígrados.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
