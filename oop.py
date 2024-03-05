import os

class Nomina:
    def __init__(self, empleado, cargo, hrjob, hrextra, hrsalario):
        self.empleado = empleado
        self.cargo = cargo
        self.hrjob = hrjob
        self.hrextra = hrextra
        self.hrsalario = hrsalario

    @staticmethod
    def edit_format(punto):
        cambio = "${:,}".format(punto)
        return cambio.replace(',', '.').replace(' ', ',')

    def calcular_nomina(self):
        if self.hrextra > 0:
            self.pagohrextra = 25000 * self.hrextra
        else:
            self.pagohrextra = 0

        self.brtotal = self.hrsalario * self.hrjob
        self.totalprepago = self.brtotal + self.pagohrextra

        self.salud = int(self.totalprepago * 0.04)
        self.pension = int(self.totalprepago * 0.04)
        self.arl = int(self.totalprepago * 0.00522)
        self.arlc = "ARL(0.522%): "

        self.totaldesc = self.salud + self.pension + self.arl
        self.totalpospago = self.totalprepago - self.totaldesc

    def imprimir(self):
        self.output.append("***************************************************")
        self.output.append("**************** VOLANTE DE PAGO ******************")
        self.output.append("***************************************************")
        self.output.append("Nombre: " + self.empleado)
        self.output.append("Cargo: " + self.cargo)
        self.output.append("Horas Trabajadas(mes): " + str(self.hrjob))
        self.output.append("Salario Bruto: " + self.edit_format(self.brtotal))
        self.output.append("Horas Extras: " + str(self.hrextra))
        self.output.append("Total pago Horas Extras: " + self.edit_format(self.pagohrextra))
        self.output.append("***************************************************")
        self.output.append("**************** DESCUENTOS DE LEY ****************")
        self.output.append("***************************************************")
        self.output.append("Salud(4%): " + self.edit_format(self.salud))
        self.output.append("Pensión(4%): " + self.edit_format(self.pension))
        self.output.append(self.arlc + self.edit_format(self.arl))
        self.output.append("Total Descuentos: " + self.edit_format(self.totaldesc))
        self.output.append("Total a Pagar: " + self.edit_format(self.totalpospago))
        self.output.append("***************************************************")
        self.output.append("************ FIN DEL VOLANTE DE PAGO **************")
        self.output.append("***************************************************")

        for line in self.output:
            print(line)

        with open('Volantes_Nomina/'+ self.empleado +'_Nomina.txt', 'w', encoding='utf-8') as archivo:
            for line in self.output:
                print(line, file=archivo)

        return print("Nomina imprimida en el documento!!")

class VolanteAdministrativo(Nomina):
    def __init__(self, empleado, hrjob, hrextra):
        super().__init__(empleado, "Auxiliar Administrativo", hrjob, hrextra, 20000)

class VolanteOperativo(Nomina):
    def __init__(self, empleado, cargo, hrjobmes):
        super().__init__(empleado, cargo, hrjobmes, 0, 40000)
        self.ibc = self.brtotal * 0.4
        self.salud = int(self.ibc * 0.125)
        self.pension = int(self.ibc * 0.16)

        if cargo == "Conductor":
            self.arl = int(self.ibc * 0.01044)
            self.arlc = "ARL(1.044%): $"
        elif cargo == "Oficios Generales":
            self.arl = int(self.ibc * 0.00522)
            self.arlc = "ARL(0.522%): $"
        elif cargo == "Vigilancia":
            self.arl = int(self.ibc * 0.04350)
            self.arlc = "ARL(4.350%): $"

        self.totaldesc = self.salud + self.pension + self.arl
        self.totalpospago = self.brtotal - self.totaldesc

class Menu:
    def __init__(self):
        self.opcion = None
        self.cargo = None

    def display(self):
        print("Impresion de Volante de Pago a Nomina.")
        print("")
        print("1. Auxiliar Administrativo ")
        print("2. Operativo(Trabajador Oficial) ")
        print("")
        self.opcion = int(input("Seleccione el Cargo del empleado: "))
        os.system("cls")

    def execute(self):
        while True: 
            if self.opcion == 1:
                empleado = input("Ingresar el nombre del empleado: ")
                hrjob = int(input("Ingresar el numero de horas laboradas(mes): "))
                hrextra = int(input("Ingresar el numero de horas extra(mes): "))
                os.system("cls")
                volante = VolanteAdministrativo(empleado, hrjob, hrextra)
            elif self.opcion == 2:
                print("Operativo(Trabajador Oficial) ")
                print("")
                print("a. Conductor ")
                print("b. Oficios Generales ")
                print("c. Vigilancia ")
                print("")
                self.cargo = input("Seleccione la especialidad del empleado: ")
                empleado = input("Ingresar el nombre del empleado: ")
                os.system("cls")
                if self.cargo == "a":
                    hrjobmes = int(160)
                elif self.cargo == "b":
                    hrjobmes = int(100)
                elif self.cargo == "c":
                    hrjobmes = int(336)
                volante = VolanteOperativo(empleado, self.cargo, hrjobmes)
            else:
                print("Numero equivocado!! Intentelo nuevamente. ")
                break

            volante.calcular_nomina()
            volante.imprimir()
            break

if __name__ == "__main__":
    menu = Menu()
    menu.display()
    menu.execute()
