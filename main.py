from rsc.modules import pacientesVet
import time

pacientesVet.crearBDD()

def app():

    registrosE = 0

    while True:
        time.sleep(1)

        print("-" * 40)
        print(" " * 7, "Veterinaria Huellitas", " " * 5)
        print("-" * 40)

        time.sleep(1)

        op = int(
            input(
                """                                                                 
            ---- Menu de Opciones ----
            
            1- Registrar Paciente
            2- Ver Todos los Registros
            3- Ver Registro por Id
            4- Modificar Registro
            5- Eliminar Registro
            6- Salir
            
            Elija una opción: """
            )
        )

        match op:
            case 1:
                print("")
                print(" " * 5, "*" * 29)
                print(" " * 7, "01 - Registro de Paciente")
                print(" " * 5, "*" * 29)

                print("")
                print("Completa el Formulario")
                print("")

                nombre = input("Nombre: ")
                sexo = input("Sexo: ")
                edad = int(input("Edad: "))
                especie = input("Especie: ")
                rasgos = input("Rasgos: ")
                enfermedad = input("Enfermedad: ")
                dueño = input("Nombre del Dueño/a: ")
                contacto = int(input("Telefono de Contacto: "))

                pacientesVet.crearPaciente(
                    nombre, sexo, edad, especie, rasgos, enfermedad, dueño, contacto
                )

                print("")
                print(" " * 5, "*" * 20)
                print(" " * 7, "Registro Exitoso")
                print(" " * 5, "*" * 20)

                print("")

                pacientesVet.tiempoClear()

            case 2:
                registros = pacientesVet.cantidadRegistros()
                
                print("")
                print(" " * 7, "02 - Todos los Registros")
                print(" " * 5, "*" * 28)

                if registros >= 1:
                    pacientesVet.leerPacientes()
                    pacientesVet.tiempoClear()
                else:
                    print("")
                    print(" ", "No hay Pacientes Registrados")
                    print("*" * 30)

                    pacientesVet.tiempoClear()

            case 3:
                registros = pacientesVet.cantidadRegistros()
                
                print("")
                print(" " * 7, "03 - Ver un Registro")
                print(" " * 5, "*" * 24)

                if registros >= 1:
                    idPaciente = int(input("Ingrese el ID del Paciente: "))
                    paciente = pacientesVet.leerPaciente(idPaciente)
                    if paciente:
                        print("\n--- Información del Paciente ---\n")
                        print(
                            f"Nombre: {paciente[0]}\nEdad: {paciente[1]}\nEspecie: {paciente[2]}\nDueño: {paciente[3]}"
                        )
                        pacientesVet.tiempoClear()
                    else:
                        print("\nEl ID no esta registrado")
                        pacientesVet.tiempoClear()

                else:
                    print("")
                    print(" ", "No hay Pacientes Registrados")
                    print("*" * 30)

                    pacientesVet.tiempoClear()

            case 4:
                registros = pacientesVet.cantidadRegistros()
                
                print("")
                print(" " * 7, "04 - Modificar un Registro")
                print(" " * 5, "*" * 30)
                
                if registros >= 1:
                    print("")
                    idPaciente = int(
                        input("Ingrese el Número del Paciente que desea modificar: ")
                    )

                    if pacientesVet.leerPaciente(idPaciente):
                    
                        print("")
                        print("Actualizando Paciente Nro: ", idPaciente)
                        print("")

                        nombre = input("Nombre: ")
                        sexo = input("Sexo: ")
                        edad = int(input("Edad: "))
                        especie = input("Especie: ")
                        rasgos = input("Rasgos: ")
                        enfermedad = input("Enfermedad: ")
                        dueño = input("Nombre del Dueño/a: ")
                        contacto = int(input("Telefono de Contacto: "))

                        if pacientesVet.actualizarPaciente(
                            idPaciente,
                            nombre,
                            sexo,
                            edad,
                            especie,
                            rasgos,
                            enfermedad,
                            dueño,
                            contacto,
                        ):
                            print("\nPaciente Actualizado")
                            pacientesVet.tiempoClear()
                    else:
                        print("\nID no Registrado")
                        pacientesVet.tiempoClear()

                else:
                    print("")
                    print(" ", "No hay Pacientes Registrados")
                    print("*" * 30)

                    pacientesVet.tiempoClear()

            case 5:
                registros = pacientesVet.cantidadRegistros()
                
                print("")
                print(" " * 7, "05 - Eliminar un Registro")
                print(" " * 5, "*" * 20)
                
                if registros >= 1:
                    print("")
                    idPaciente = int(
                        input("Ingrese el Número de Paciente que desea eliminar: ")
                    )
                    if pacientesVet.eliminarPaciente(idPaciente):
                        print("\n¡Paciente Eliminado!")
                        pacientesVet.tiempoClear()
                        registrosE += 1
                    else:
                        print("\n¡Error al Eliminar!")
                        pacientesVet.tiempoClear()
                else:
                    print("")
                    print(" ", "No hay Pacientes Registrados")
                    print("*" * 30)

                    pacientesVet.tiempoClear()

            case 6:
                registros = pacientesVet.cantidadRegistros()
                
                print("")
                print(" " * 5, "*" * 20)
                print(" " * 6, "06 - Reporte Final")
                print(" " * 5, "*" * 20)

                print(f"\nEl sistema tiene {registros} Pacientes Registrados.")
                print(f"\nSe eliminaron durante esta sesión {registrosE} Paciente/s.")
                print("\n--- FIN DEL PROGRAMA ---")
                break

            case _:
                print(
                    """
                      ¡Opción Invalida!
                      
                      Regresando al menu principal...                      
                      """
                )

                pacientesVet.tiempoClear()


if __name__ == "__main__":
    app()
