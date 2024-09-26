import os
from tkinter import Variable
x = 0
y = 0
os.system("clear")
campus = ("zona core", "campus uno", "campus matriz", "sector outsourcing")
print ("que quiere hacer? ")
print("1. Ver los dispositivos. \n2. Ver los campus. \n3. Añadir dispositivo. \n4 Añadir campus. \n5 Borrar dispositivo. \6 Borrar campus")
selector = int()
selector = input("elegir una opcion")
if int (selector) == 1:
    os.system("clear")
    y = 1
    selector = int()
    print("elijir un campus \n")
    while len (campus)>=y:
        for item in campus:
         print(str(y)+".", item)
         y=y+1
    selector = input ("\n Elija una opcion: ")
    x = int()
    x = int(selector)-1
    if int(x) >= 0:
            os.system("clear")
            file= open(campus[int(x)]+".txt", "r")
            for item in file:
                item=item.strip()
                print (item)
                file.close()
elif int (selector)==2:
    os.system ("clear")
    y = 1
    selector = int()
    while len(campus)>=y:
        for item in campus:
            print(str(y)+".", item)
            y=y+1
elif int (selector)==2:
    os.system ("clear")
    y = 1
    selector = int()
    servicios = []
    print("¿Donde agregar nuevo dispositivo? \n")
    while len(campus)>=y:
        for item in campus:
            print (str(y)+".", item)
            y=y+1
    selector = input("\n Elija una opcion: ")
    x = int()
    x = int(selector)-1
    if int(x) >=0:
        os.system("clear")
        file=open(campus[int(x)]+".txt", "a")
        print ("elija un dispositivo: \n \n1. Router. \n2. Switch. \n3. Switch multicapa. \n")
        variable1 = input("Elija su opcion: ")
        os.system("clear")
        print("Agregue el nombre de su dispositivo")
        variable2 = input("Agregue su nombre: ")
        while True:
            print("¿Confirma este nombre? \n \n1. Si \n2. No \n")
            variable3 = input("introduzca su respuesta")
            if variable3 == "1":
                print ("terminado")
                break
        print("Elija una jerarquia: \n \n1. Nucleo, \n2. Acceso. \n3. Distribucion. \n")
        variable3 = input("Elija una opcion: ")
        os.system("clear")
        file.write("\n---------------------------------\n")
        if int(variable1) ==1:
            print("Elija un servicio de red para el switch: \n1. Datos \n2. VLAN \n3. Trunking \n4. Salir \n")
            variable4 = int()
            while variable4 != 4:
                variable4 = int(input("Elija una opcion"))
                if variable4 == 1:
                    servicios.append("Datos")
                elif variable4 == 2:
                    servicios.append("VLAN")
                elif variable4 == 3:
                 servicios.append("Trunking")
            file.write("Switch: " + variable2)
            if int (variable3) == 1:
                file.write("\nJerarquia: Nucleo")
            elif int(variable3) ==2:
                file.write("\nJerarquia: Distribucion")
            elif int (variable3) == 3:
                file.write("\nJerarquia Acceso")
            file.write("\Servicio: "+str(servicios))
        elif int(variable1) ==2:
           print("Elija un servicio de red para multicapa: \n1. Datos \n2. VLAN \n3. Trunking \n4. Enrutamiento \n5. Salir")
           variable4 = int()
           while variable4 != 5:
                variable4 = int(input("Elija una opcion: "))
                if variable4 == 1:
                    servicios.append("Datos")
                elif variable4 == 2:
                    servicios.append("VLAN")
                elif variable4 == 3:
                    servicios.append("Trunking")
                elif variable4 == 4:
                    servicios.append("Enrutamiento")
        file.write("Switch multicapa: " + variable2)
        if int(variable3) == 1:
                file.write("\nJerarquia: Nucleo")
        elif int(variable3) == 2:
                file.write("\nJerarquia: Distribucion")
        elif int(variable3) == 3:
                file.write("\nJerarquia: Acceso")
        file.write("\nServicio: "+ str(servicios))
    elif int(variable1) == 3:
        variable4 = int()
        print ("Elija un servicio de red para el router: \n1. Enrutamiento \n2. Salir") 
        while variable4 != 2:
            variable4 = int(input("Elija una opcion: "))
            if variable4 == 1:
                servicios.append("Datos")
    file.write("Router: "+ variable2)
    if int(variable3) ==1:
        file.write("\nJerarquia: Nucleo")
    elif int(variable3) ==2:
        file.write("\nJerarquia: Distribucion")
    elif int(variable3) ==3:
        file.write("\nJerarquia: Acceso")
file.write("\nServicio: "+ str(servicios))
file.write("\n---------------------------------\n")
file.close()





