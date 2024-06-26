#Ejercicio01
def Ejercicio01():
    '''Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. 
    ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? 
    Realice el algoritmo y represente la solución mediante el diagrama de flujo, el 
    pseudocódigo y el diagrama N/S, utilizando el ciclo apropiado.'''

    #Definir Variables
    acumuladorsalario=0.0

    # Ingresar Datos    
    tiempo=int(input("Ingrese los años disponible del incremento: "))
    salario=float(input(f"Ingrese su salario: "))
    #Calcular salario
    for x in range(tiempo+1):
        if x==0:
            print(f"El Salario total del año {x} es ",salario, " dolares")
        else:   
            incremeto=salario*0.10
            salarioTotal= salario+incremeto
            salario=salarioTotal
            if x!=tiempo:
                print(f"El Salario total del año {x} es ", round(salarioTotal,2), " dolares")
            else:
                print("")
                print(f"El ultimo salario  a percibir del año {x} es de ", round(salarioTotal,2), "dolares")
            acumuladorsalario+=salarioTotal
    #El salario total
    print("")
    print()
    print(f"El salario total recibido durante los {tiempo} años fue de: ",round(acumuladorsalario,2),"dolares")
    print("")
#Ejercicio02
def Ejercicio02():
    '''Realice y represente mediante diagrama de flujo y pseudocódigo un
    algoritmo que lea los nombres y las edades de diez alumnos, y que los
    datos se almacenen en dos vectores, y con base en esto se determine
    el nombre del alumno con la edad mayor del arreglo.'''
    #definicion de variables 
    tama = 10
    nom_Al = []
    ed_Al = []
    mayor = 0
    pos = 0
    def llenar():
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del alumno: "))
        return nombre,edad

    def mayor_Al(ed_Al):
        for x in range(len(ed_Al)):
            if x == 0:
                if ed_Al[x]> ed_Al[x+1]:
                    mayor = ed_Al[x]
                    pos = x
                else :
                    mayor = ed_Al[x+1]
                    pos = x+1
            else :
                if ed_Al[x]> mayor:
                    mayor = ed_Al[x]
                    pos = x
        return mayor, pos

    def mainEjerecicio02():
        print("CALCULO DE EDADES")
        for a in range(tama):
            print("Ingrese del alumno #",a+1)
            nombre,edad = llenar()
            nom_Al.append(nombre)
            ed_Al.append(edad)
        mayor,pos = mayor_Al(ed_Al)
        print()
        print(f"El alumno con mayor edad es {nom_Al[pos]} y su edad es: {mayor}")

    return mainEjerecicio02()
#Opciones
def opciones(opc):
        if opc==1:
            Ejercicio01()
        elif opc==2:    
            Ejercicio02()      
        print("-------Menu Ejercicio---------")
        print("1) Ejercicio 01")
        print("2) Ejercicio 02")
        print("3) Salir")
        opc=int(input("Ingrese una opcion: "))
        return opc
#Funcion Principal
def main():
    print("-------Menu Ejercicio---------")
    print("1) Ejercicio 01")
    print("2) Ejercicio 02")
    print("3) Salir")
    opc=int(input("Ingrese una opcion: "))
    while(opc!=3):
        opc=opciones(opc)
    print("Muchas gracias ")
#Llamar la funcion principal:
main()
