import volantesyformulas as cc
import os

def menu():

    print("Impresion de Volante de Pago a Nomina.")
    print("")
    print("1. Auxiliar Administrativo ")
    print("2. Operativo(Trabajador Oficial) ")
    print("")
    opcion = int(input("Seleccione el Cargo del empleado: "))
    os.system("cls")


    while True: 
        if opcion == 1:
            cc.volante_administrativo()
        elif opcion == 2:
            print("Operativo(Trabajador Oficial) ")
            print("")
            print("a. Conductor ")
            print("b. Oficios Generales ")
            print("c. Vigilancia ")
            print("")
            cargo = input("Seleccione la especialidad del empleado: ")

            if cargo == "a":
                cc.volante_operativo(cargo = "Conductor")
            elif cargo == "b":   
                cc.volante_operativo(cargo = "Oficios Generales")
            elif cargo == "c":
                cc.volante_operativo(cargo = "Vigilancia")
            else :
                print("Opcion no valida")
        else:
            print("Numero equivocado!! Intentelo nuevamente. ")
        break
menu()