# -*- coding: utf-8 -*-
"""entrega finalipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zvdA8X90KroLXbrGb8u6kj2yRCEyWVKy
"""

import re
import datetime

usuarios = {}
vehiculos = {}
ingresos = {}
retiros = []
ADMIN_CREDENCIALES = {'administradores': '1234'}
PRECIO_HORA = 7000
PRECIO_CUARTO = 1500
parqueadero = "Easy Parking - Rápido, sencillo y a tu medida"

def validar_nombre(texto):
    return texto.isalpha() and len(texto) >= 3

def validar_documento(doc):
    return doc.isdigit() and 3 <= len(doc) <= 15

def validar_placa(placa):
    return bool(re.match(r'^[A-Z]{3}[0-9]{3}$', placa.upper()))

def registrar_usuario():
    print("\n Registrar Usuario")
    nombre = input("Nombre: ").strip()
    if not validar_nombre(nombre):
        print("Nombre inválido.")
        return
    apellido = input("Apellido: ").strip()
    if not validar_nombre(apellido):
        print("Apellido inválido.")
        return
    documento = input("Documento: ").strip()
    if not validar_documento(documento):
        print("Documento inválido.")
        return
    placa = input("Placa del vehículo (AAA111): ").upper().strip()
    if not validar_placa(placa):
        print("Placa inválida.")
        return
    if documento in usuarios:
        print("Usuario ya registrado.")
        return
    usuarios[documento] = {
        'nombre': nombre,
        'apellido': apellido,
        'placa': placa
    }
    vehiculos[placa] = documento
    print("Usuario registrado exitosamente.")

def ingresar_vehiculo():
    print("\n Ingreso de Vehículo")
    documento = input("Documento del usuario: ").strip()
    if documento not in usuarios:
        print("Usuario no registrado.")
        return
    placa = input("Placa del vehículo: ").upper().strip()
    if placa not in vehiculos or vehiculos[placa] != documento:
        print("Vehículo no registrado o no pertenece al usuario.")
        return
    if placa in ingresos:
        print("Este vehículo ya está ingresado.")
        return
    hora_ingreso = datetime.datetime.now()
    ingresos[placa] = hora_ingreso
    print(f"Ingreso registrado a las {hora_ingreso.strftime('%H:%M:%S')}")
    print(f" Recibo \nUsuario: {usuarios[documento]['nombre']} {usuarios[documento]['apellido']}\nPlaca: {placa}\nHora ingreso: {hora_ingreso}")

def retirar_vehiculo():
    print("\n--- Retiro de Vehículo ---")
    placa = input("Placa del vehículo: ").upper().strip()
    if placa not in ingresos:
        print("El vehículo no está en el parqueadero.")
        return
    hora_salida = datetime.datetime.now()
    hora_entrada = ingresos.pop(placa)
    duracion = hora_salida - hora_entrada
    total_min = duracion.total_seconds() / 60
    horas = int(total_min // 60)
    cuartos = int((total_min % 60) // 15)
    total_pagar = max(PRECIO_HORA, horas * PRECIO_HORA + cuartos * PRECIO_CUARTO)
    documento = vehiculos[placa]
    retiros.append({
        'placa': placa,
        'documento': documento,
        'entrada': hora_entrada,
        'salida': hora_salida,
        'tiempo': duracion,
        'pago': total_pagar
    })
    print(f"Vehículo retirado. Tiempo: {duracion}, Total a pagar: ${total_pagar}")

def admin_menu():
    print("\n Acceso Administrador")
#    print("Seleccione el administrador:")
    usuario = input("Usuario admin: ")
    contraseña = input("Contraseña: ")
    if ADMIN_CREDENCIALES.get(usuario) != contraseña:
        print("Credenciales incorrectas.")
        return

    while True:
        print("\n Menú Administrador ")
        print("1. Total de vehículos registrados")
        print("2. Total de vehículos retirados")
        print("3. Total de vehículos sin retirar")
        print("4. Total pago de vehículos retirados")
        print("5. Tiempo promedio de estancia")
        print("6. Lista de usuarios")
        print("7. Vehículo con tiempo máximo y mínimo")
        print("8. Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            print(f"Total registrados: {len(vehiculos)}")
        elif op == "2":
            print(f"Total retirados: {len(retiros)}")
        elif op == "3":
            print(f"Vehículos sin retirar: {len(ingresos)}")
        elif op == "4":
            total = sum(r['pago'] for r in retiros)
            print(f"Total pagado: ${total}")
        elif op == "5":
            if retiros:
                prom = sum(r['tiempo'].total_seconds() for r in retiros) / len(retiros)
                print(f"Promedio estancia: {datetime.timedelta(seconds=prom)}")
            else:
                print("No hay retiros aún.")
        elif op == "6":
            for doc, datos in usuarios.items():
                print(f"{doc}: {datos['nombre']} {datos['apellido']} - {datos['placa']}")
        elif op == "7":
            if retiros:
                max_v = max(retiros, key=lambda x: x['tiempo'])
                min_v = min(retiros, key=lambda x: x['tiempo'])
                print(f"Mayor tiempo: {max_v['placa']} - {max_v['tiempo']}")
                print(f"Menor tiempo: {min_v['placa']} - {min_v['tiempo']}")
            else:
                print("No hay datos.")
        elif op == "8":
            break
        else:
            print("Opción inválida.")

def main():
    print(f'\nBienvenido al parqueadero "{parqueadero}"')
    while True:
        print("\n Menú Principal ")
        print("1. Registrar usuario")
        print("2. Ingresar vehículo")
        print("3. Retirar vehículo")
        print("4. Administrador")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            ingresar_vehiculo()
        elif opcion == "3":
            retirar_vehiculo()
        elif opcion == "4":
            admin_menu()
        elif opcion == "5":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

# csv_export.py

import csv
import os

# Crea archivos si no existen
def inicializar_archivos():
    if not os.path.exists("usuarios.csv"):
        with open("usuarios.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Documento", "Nombre", "Apellido", "Placa"])
    if not os.path.exists("retiros.csv"):
        with open("retiros.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Placa", "Documento", "Entrada", "Salida", "Duración", "Pago"])

# Escribe usuario en usuarios.csv
def guardar_usuario_csv(documento, nombre, apellido, placa):
    with open("usuarios.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([documento, nombre, apellido, placa])

# Escribe retiro en retiros.csv
def guardar_retiro_csv(placa, documento, entrada, salida, duracion, pago):
    with open("retiros.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([placa, documento, entrada, salida, duracion, pago])

from google.colab import files
inicializar_archivos()
# Descargar los archivos CSV creados
files.download ('usuarios.csv')
files.download ('retiros.csv')