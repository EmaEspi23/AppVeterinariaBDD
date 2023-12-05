import sqlite3
import time
import os
import datetime as dt


def crearBDD():
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Paciente (
            idPaciente INTEGER,
            Nombre TEXT,
            Sexo TEXT,
            Edad INTEGER,
            Especie TEXT,
            Rasgos TEXT,
            Enfermedad TEXT,
            Dueño TEXT,
            Contacto INTEGER,
            PRIMARY KEY("idPaciente" AUTOINCREMENT)
        )
    """
    )

    conexion.commit()
    conexion.close()


def crearPaciente(nombre, sexo, edad, especie, rasgos, enfermedad, dueño, contacto):
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO Paciente (Nombre, Sexo, Edad, Especie, Rasgos, Enfermedad, Dueño, Contacto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (nombre, sexo, edad, especie, rasgos, enfermedad, dueño, contacto),
    )

    conexion.commit()
    conexion.close()


def leerPaciente(idPaciente):
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        SELECT nombre, edad, especie, dueño FROM Paciente WHERE idPaciente = ?
    """,
        (idPaciente,),
    )

    paciente = cursor.fetchone()
    conexion.close()
    return paciente


def leerPacientes():
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT idPaciente, nombre, edad FROM Paciente")

    pacientes = cursor.fetchall()

    for aux in pacientes:
        print(f"ID: {aux[0]} - Nombre {aux[1]} - Edad: {aux[2]}")

    conexion.close()


def actualizarPaciente(
    idPaciente, nombre, sexo, edad, especie, rasgos, enfermedad, dueño, contacto
):
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE Paciente
        SET Nombre = ?, Sexo = ?, Edad = ?, Especie = ?, Rasgos = ?, Enfermedad = ?, Dueño = ?, Contacto = ?
        WHERE idPaciente = ?
    """,
        (nombre, sexo, edad, especie, rasgos, enfermedad, dueño, contacto, idPaciente),
    )

    filasAfectadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    return filasAfectadas


def eliminarPaciente(idPaciente):
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM Paciente WHERE idPaciente = ?", (idPaciente,))

    filasAfectadas = cursor.rowcount
    conexion.commit()
    conexion.close()
    return filasAfectadas

def cantidadRegistros():
    conexion = sqlite3.connect("Veterinaria.db")
    cursor = conexion.cursor()

    cursor.execute('SELECT COUNT(*) FROM Paciente')

    registros = cursor.fetchone()[0]
    
    conexion.close()

    return registros
        

def tiempoClear():
    time.sleep(4)
    os.system("cls")
