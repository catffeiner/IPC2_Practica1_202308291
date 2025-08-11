from LibroDigital import Digital
from LibroFisico import Fisico

if __name__ == "__main__":

    LibroDigital: 0
    LibroFisico: 0

    while True:
        print("\n ------------ Menu de Biblioteca ------------")
        print("1. Registrar nuevo material físico o digital")
        print("2. Gestionar material")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del material: ")
            autor = input("Ingrese el autor del material: ")

        if opcion == "2":
            print("\n ----------- Gestionar Material -----------")
            print("1. Material registrado")
            print("2. Prestar material")
            print("3. Devolver material")
            print("4. Consultar material")
            print("5. Regresar al menú principal")
            opciongestion = input("Seleccione una opción: ")

            if opciongestion == "1":
                print("\n ----------- Material Registrado -----------")
                if LibroDigital == 0 and LibroFisico == 0:
                    print("No hay material registrado.")
                else:
                    if LibroDigital != 0:
                        print(f"Material Digital: {LibroDigital.mostrarInformacion()}")
                    if LibroFisico != 0:
                        print(f"Material Físico: {LibroFisico.mostrarInformacion()}")

            if opciongestion == "2":

            if opciongestion == "3":

            if opciongestion == "4":

            if opciongestion == "5":
                continue

        if opcion == "3":
            print("Saliendo de la aplicación...")
            break