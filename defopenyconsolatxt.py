def edit_format(punto):
    cambio = "${:,}".format(punto)
    return cambio.replace(',', '.').replace(' ', ',')

def imprimir_nomina(empleado,cargo,hrjb,salbr,he,tphe,salud,pension,arl,totalpospago):
    with open('nomina/nomina.txt', 'a', encoding='utf-8') as archivo:
        with open('nomina/nomina.txt', 'r', encoding='utf-8') as archivo_lectura:
            lineas = archivo_lectura.readlines()
            if lineas == []:
                #TIENE QUE FUNCIONAR ༼ つ ◕_◕ ༽つ
                encabezado = '║ '+"Nombre".center(32) +'║ '+ "Cargo".center(25)+'║ '+ "HT".center(6) +'║ '+ "Salario".center(14) +'║ '+ "HE".center(6) +'║ '+ "TPHE".center(15) +'║ '+ "Salud".center(14) +'║ '+ "Pensión".center(14) +'║ '+ "ARL".center(14) +'║ '+ "Total a Pagar".center(20)+'║'            
                archivo.write('–' * len(encabezado) + '\n')
                archivo.write(encabezado + '\n')
                archivo.write('–' * len(encabezado) + '\n')
        #PROfinnsAAAAAAAAA (☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)
        datos_empleado = '║ ' + empleado.center(32)+'║ '+cargo.center(25)+'║ '+str(hrjb).center(6)+'║ '+edit_format(salbr).center(14)+'║ '+str(he).center(6)+'║ '+edit_format(tphe).center(15)+'║ '+edit_format(salud).center(14)+'║ '+edit_format(pension).center(14)+'║ '+edit_format(arl).center(14)+'║ '+edit_format(totalpospago).center(20)+'║'
        archivo.write(datos_empleado + '\n')
        archivo.write('–' * len(datos_empleado) + '\n')

def consola_print(empleado,cargo,hrjb,salbr,he,tphe,salud,pension,arl,totaldesc,totalpospago,arlc):

    print("***************************************************")
    print("**************** VOLANTE DE PAGO ******************")
    print("***************************************************")
    print("Nombre: ", empleado)
    print("Cargo: ", cargo)
    print("Horas Trabajadas(mes): ", hrjb)
    print("Salario Bruto: ", edit_format(salbr))
    print("Horas Extras: ", he)
    print("Total pago Horas Extras: ", edit_format(tphe))
    print("***************************************************")
    print("**************** DESCUENTOS DE LEY ****************")
    print("***************************************************")
    print("Salud(4%): ", edit_format(salud))
    print("Pensión(4%): ", edit_format(pension))
    print(arlc, edit_format(arl))
    print("Total Descuentos: ", edit_format(totaldesc))
    print("Total a Pagar: ", edit_format(totalpospago))
    print("***************************************************")
    print("************ FIN DEL VOLANTE DE PAGO **************")
    print("***************************************************")

    with open('Volantes_Nomina/'+ empleado +'_Nomina.txt', 'w', encoding='utf-8') as archivo:
        print("***************************************************", file = archivo)
        print("**************** VOLANTE DE PAGO ******************", file = archivo)
        print("***************************************************", file = archivo)
        print("Nombre: ", empleado, file = archivo)
        print("Cargo: ", cargo, file = archivo)
        print("Horas Trabajadas(mes): ", hrjb, file = archivo)
        print("Salario Bruto: ", edit_format(salbr), file = archivo)
        print("Horas Extras: ", he, file = archivo)
        print("Total pago Horas Extras: ", edit_format(tphe), file = archivo)
        print("***************************************************", file = archivo)
        print("**************** DESCUENTOS DE LEY ****************", file = archivo)
        print("***************************************************", file = archivo)
        print("Salud(4%): ", edit_format(salud), file = archivo)
        print("Pensión(4%): ", edit_format(pension), file = archivo)
        print(arlc, edit_format(arl), file = archivo)
        print("Total Descuentos: ", edit_format(totaldesc), file = archivo)
        print("Total a Pagar: ", edit_format(totalpospago), file = archivo)
        print("***************************************************", file = archivo)
        print("************ FIN DEL VOLANTE DE PAGO **************", file = archivo)
        print("***************************************************", file = archivo)
