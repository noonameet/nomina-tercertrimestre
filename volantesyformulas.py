import os
import defopenyconsolatxt as pri

def volante_administrativo():

    print("Auxiliar Administrativo ")
    print("")
    empleado = input("Ingresar el nombre del empleado: ")
    cargo = "Auxiliar Administrativo"
    hrjob = int(input("Ingresar el numero de horas laboradas(mes): "))
    hrextra = int(input("Ingresar el numero de horas extra(mes): "))
    os.system("cls")
    hrsalario = int(20000)

    #Condicional para hallar el pago total de horas extra 
    if hrextra > 0:
        pagohrextra = 25000 * hrextra
    else:
        pagohrextra = 0

    #Calculos de Nomina
    #Salario bruto + Total pago extra
    brtotal = hrsalario * hrjob
    totalprepago = brtotal + pagohrextra
    
    #Descuentos de Ley
    #Salud(4%)
    salud = int(totalprepago * 0.04) 
    #Pensión(4%)
    pension = int(totalprepago * 0.04)
    #ARL(0.522%)
    arl = int(totalprepago * 0.00522)
    arlc = "ARL(0.522%): "
    #Total descuento
    totaldesc = salud + pension + arl 

    #Total a Pagar en la Nomina
    totalpospago = totalprepago - totaldesc

    pri.consola_print(empleado,cargo,hrjob,brtotal,hrextra,pagohrextra,salud,pension,arl,totaldesc,totalpospago,arlc)
       
    pri.imprimir_nomina(empleado,cargo,hrjob,brtotal,hrextra,pagohrextra,salud,pension,arl,totalpospago)
        
    return print("Nomina imprimida en el documento!!") 

def volante_operativo(cargo):

    empleado = input("Ingresar el nombre del empleado: ")
    os.system("cls")
    if cargo == "Conductor":
        hrjobmes = int(160)
    elif cargo == "Oficios Generales":
        hrjobmes = int(100)
    elif cargo == "Vigilancia":
        hrjobmes = int(336)

    hrsalario = 40000

    #Salario bruto + Total pago extra
    brtotal = hrsalario * hrjobmes

    ibc = brtotal * 0.4

    he = 0
    tphe = 0
     
    #Descuentos de Ley
    #Salud(12.5%)
    salud = int(ibc * 0.125) 
    #Pensión(16%)
    pension = int(ibc * 0.16)

    #ARL
    if cargo == "Conductor":
        #ARL Conductor Riesgo II: (1.044%)
        arl = int(ibc * 0.01044)
        arlc = "ARL(1.044%): $"
    elif cargo == "Oficios Generales":
        #ARL Conductor Riesgo I: (0.522%)
        arl = int(ibc * 0.00522)
        arlc = "ARL(0.522%): $"
    elif cargo == "Vigilancia":
        #ARL Conductor Riesgo IV: (4.350%)
        arl = int(ibc * 0.04350)
        arlc = "ARL(4.350%): $"

    #Total descuento
    totaldesc = salud + pension + arl 

    #Total a Pagar en la Nomina
    totalpospago = brtotal - totaldesc

    pri.consola_print(empleado,cargo,hrjobmes,brtotal,he,tphe,salud,pension,arl,totaldesc,totalpospago,arlc)

    pri.imprimir_nomina(empleado,cargo,hrjobmes,brtotal,he,tphe,salud,pension,arl,totalpospago)
            
    return print("Nomina imprimida en el documento!!") 