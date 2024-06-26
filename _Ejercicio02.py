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

def main():
    print("CALCULO DE EDADES")
    for a in range(tama):
        print("Ingrese del alumno #",a+1)
        nombre,edad = llenar()
        nom_Al.append(nombre)
        ed_Al.append(edad)
    mayor,pos = mayor_Al(ed_Al)
    print()
    print(f"El alumno con mayor edad es {nom_Al[pos]} y su edad es: {mayor}")
main()