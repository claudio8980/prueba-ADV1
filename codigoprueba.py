import os
import ipaddress

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("¿Qué quiere hacer?")
    print("1. Ver los dispositivos.")
    print("2. Ver los campus.")
    print("3. Añadir dispositivo.")
    print("4. Añadir campus.")
    print("5. Borrar dispositivo.")
    print("6. Borrar campus.")

def listar_campus(campus):
    for i, item in enumerate(campus, start=1):
        print(f"{i}. {item}")

def ver_dispositivos(campus):
    clear_screen()
    listar_campus(campus)
    try:
        selector = int(input("\nElija una opción: ")) - 1
        if 0 <= selector < len(campus):
            with open(campus[selector] + ".txt", "r") as file:
                for line in file:
                    print(line.strip())
        else:
            print("Selección inválida.")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")

def validar_ip(direccion_ip):
    try:
        ip = ipaddress.ip_address(direccion_ip)
        if ip.version == 4:
            return "IPv4"
        elif ip.version == 6:
            return "IPv6"
    except ValueError:
        return None

def agregar_dispositivo(campus):
    clear_screen()
    listar_campus(campus)
    
    try:
        selector = int(input("\nElija un campus donde agregar el dispositivo: ")) - 1
        if 0 <= selector < len(campus):
            with open(campus[selector] + ".txt", "a") as file:
                # Elegir tipo de dispositivo
                print("Elija un dispositivo:\n1. Router\n2. Switch\n3. Switch multicapa")
                dispositivo = input("Elija su opción: ")

                # Nombre del dispositivo
                nombre_dispositivo = input("Agregue el nombre de su dispositivo: ")

                # Confirmar nombre del dispositivo
                while True:
                    confirmacion = input(f"¿Confirma este nombre '{nombre_dispositivo}'? (1. Sí / 2. No): ")
                    if confirmacion == "1":
                        break
                    elif confirmacion == "2":
                        nombre_dispositivo = input("Agregue el nombre de su dispositivo: ")

                # Ingresar jerarquía
                print("Elija una jerarquía:\n1. Núcleo\n2. Acceso\n3. Distribución")
                jerarquia = input("Elija una opción: ")

                # Ingresar direccionamiento IP y validarlo
                while True:
                    direccion_ip = input("Ingrese el direccionamiento IP del dispositivo: ")
                    tipo_ip = validar_ip(direccion_ip)
                    if tipo_ip:
                        print(f"La IP ingresada es válida y es {tipo_ip}.")
                        break
                    else:
                        print("La dirección IP ingresada no es válida. Intente nuevamente.")

                # Guardar la información en el archivo
                file.write("\n---------------------------------\n")
                file.write(f"Dispositivo: {nombre_dispositivo}\n")
                file.write(f"Dirección IP: {direccion_ip} ({tipo_ip})\n")

                if dispositivo == "1":
                    file.write("Tipo: Router\n")
                elif dispositivo == "2":
                    file.write("Tipo: Switch\n")
                elif dispositivo == "3":
                    file.write("Tipo: Switch multicapa\n")

                if jerarquia == "1":
                    file.write("Jerarquía: Núcleo\n")
                elif jerarquia == "2":
                    file.write("Jerarquía: Acceso\n")
                elif jerarquia == "3":
                    file.write("Jerarquía: Distribución\n")

                file.write("---------------------------------\n")
                print("Dispositivo añadido correctamente.")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Por favor ingrese un número válido.")
    except FileNotFoundError:
        print("El archivo para este campus no existe.")

def main():
    campus = ("zona core", "campus uno", "campus matriz", "sector outsourcing")
    while True:
        clear_screen()
        mostrar_menu()
        
        try:
            selector = int(input("Elija una opción: "))
            if selector == 1:
                ver_dispositivos(campus)
            elif selector == 2:
                clear_screen()
                listar_campus(campus)
            elif selector == 3:
                agregar_dispositivo(campus)
            elif selector == 4:
                print("Funcionalidad no implementada aún.")
            elif selector == 5:
                print("Funcionalidad no implementada aún.")
            elif selector == 6:
                print("Funcionalidad no implementada aún.")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor ingrese un número válido.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()

