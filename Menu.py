from LibroDigital import Digital
from LibroFisico import Fisico

if __name__ == "__main__":
    libroDigital = None
    libroFisico = None

    while True:
        print("\n ------------ Menú de Biblioteca ------------")
        print("1. Registrar nuevo material físico o digital")
        print("2. Gestionar material")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("¿Qué tipo de material desea registrar?")
            print("1. Libro Digital")
            print("2. Libro Físico")
            tipo = input("Seleccione una opción: ")
            titulo = input("Ingrese el título del material: ")
            autor = input("Ingrese el autor del material: ")

            if tipo == "1":
                tamaño = int(input("Ingrese el tamaño del archivo en MB: "))
                libroDigital = Digital(titulo, autor, tamaño)
                print("Libro digital registrado")

            elif tipo == "2":
                ejemplares = input("Ingrese el número de ejemplares: ")
                libroFisico = Fisico(titulo, autor, ejemplares)
                print("Libro físico registrado")

        elif opcion == "2":
            print("\n ----------- Gestionar Material -----------")
            print("1. Material registrado")
            print("2. Prestar material")
            print("3. Devolver material")
            print("4. Consultar material")
            print("5. Regresar al menú principal")
            opciongestion = input("Seleccione una opción: ")

            if opciongestion == "1":
                if not libroDigital and not libroFisico:
                    print("No hay material registrado.")
                else:
                    if libroDigital:
                        libroDigital.mostrarInformacion()
                    if libroFisico:
                        libroFisico.mostrarInformacion()

            elif opciongestion == "2":
                codigo = input("Ingrese el código único del material a prestar: ")
                if libroDigital and libroDigital.get_codigounico() == codigo:
                    libroDigital.prestarMaterial()
                elif libroFisico and libroFisico.get_codigounico() == codigo:
                    libroFisico.prestarMaterial()
                else:
                    print("Material no encontrado")

            elif opciongestion == "3":
                codigo = input("Ingrese el código único del material a devolver: ")
                if libroDigital and libroDigital.get_codigounico() == codigo:
                    libroDigital.devolverMaterial()
                elif libroFisico and libroFisico.get_codigounico() == codigo:
                    libroFisico.devolverMaterial()
                else:
                    print("Material no encontrado")

            elif opciongestion == "4":
                codigo = input("Ingrese el código único del material a consultar: ")
                if libroDigital and libroDigital.get_codigounico() == codigo:
                    libroDigital.mostrarInformacion()
                elif libroFisico and libroFisico.get_codigounico() == codigo:
                    libroFisico.mostrarInformacion()
                else:
                    print("Material no encontrado")

        elif opcion == "3":
            print("Saliendo de la aplicación...")
            break