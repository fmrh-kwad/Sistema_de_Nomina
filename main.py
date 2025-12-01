import os
import reportes

#------------------------------------#
# GRUPO 3:
# LYA FERRERAS
# FRANK RUIZ
# STEVEN CRUZ
# MAXIMILIAM NOVOA
#------------------------------------#

# Códigos de colores y formato
NEGRITA = '\033[1m'
ITALICA = '\033[3m'
RESET = '\033[0m'
n = 'numero'

# Funciones para pedir datos del usuario, asegurandose de que se ingresen valores validos para que el programa no explote 🥀
def solicitar_num(mensaje, minimo = None):
    # Se asegura de que el usuario ponga un float (numero) valido
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El numero no puede ser menor que {minimo}.")
                continue
            return valor
        except ValueError:
            print("Por favor escriba un numero valido")


def solicitar_str(mensaje):
    # Se asegura de que el usuario ingrese una string no vacio
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("El valor no puede estar vacio.")
        else:
            return valor

#------------------------------------#
# Funcion para limpiar la terminal
def limpiar_terminal():
    if os.name == 'nt': ## Si el usuario tiene windows
        os.system('cls')
    else: ## Si se usa mac o linux
        os.system('clear')
#------------------------------------#

#------------------------------------#
# FUNCIONES DE EMPLEADOS
def registrar_empleado(empleados):
    print("===============================")
    print("Registrar empleado")
    print("===============================")
    empleado_id = solicitar_str("ID del empleado: ")

    if empleado_id in empleados:
        print("\nYa existe un empleado con ese ID.")
        input("Presione ENTER para regresar")
        return

    nombre = solicitar_str("Nombre del empleado: ")
    salario_hora = solicitar_num("Salario por hora: ", minimo=0)

    empleados[empleado_id] = {
        "nombre": nombre,
        "salario_hora": salario_hora,
        "horas_trabajadas": 0.0,
        "horas_extra": 0.0,
        "pago_bruto": 0.0,
        "deducciones": 0.0,
        "pago_neto": 0.0,
    }

    print(f"\nEmpleado {NEGRITA}{ITALICA}{nombre} {RESET}registrado correctamente.")
    input("Presione ENTER para regresar")



def actualizar_salario(empleados):
    print("===============================")
    print("Actualizar salario")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return

    empleado_id = solicitar_str("ID del empleado: ")
    if empleado_id not in empleados:
        print("\nEmpleado no encontrado.")
        input("Presione ENTER para regresar")
        return

    nuevo_salario = solicitar_num("Nuevo salario por hora: ", minimo=0)
    empleados[empleado_id]["salario_hora"] = nuevo_salario

    print("\nSalario actualizado correctamente.")
    input("Presione ENTER para regresar")


def registrar_horas(empleados):
    print("===============================")
    print("Registrar horas")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return

    empleado_id = solicitar_str("ID del empleado: ")
    if empleado_id not in empleados:
        print("\nEmpleado no encontrado.")
        input("Presione ENTER para regresar")
        return

    horas_normales = solicitar_num("Horas trabajadas (normales): ", minimo=0)
    horas_extra = solicitar_num("Horas extra: ", minimo=0)

    empleados[empleado_id]["horas_trabajadas"] = horas_normales
    empleados[empleado_id]["horas_extra"] = horas_extra

    print("\nHoras registradas correctamente.")
    input("Presione ENTER para regresar")


def calcular_pagos(empleados, factor_hora_extra=1.5):
    print("===============================")
    print("Calcular pagos")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return
    
    for emp_id, datos in empleados.items():
        salario = datos["salario_hora"]
        h_normales = datos["horas_trabajadas"]
        h_extra = datos["horas_extra"]

        pago_normales = salario * h_normales
        pago_extra = salario * factor_hora_extra * h_extra
        pago_bruto = pago_normales + pago_extra

        # Deducciones por el seguro y la afp
        # 3.04% Seguro Familiar de Salud (SFS)
        # 2.87% de la AFP (Administradora de Fondo de Pensiones)
        deduccion_afp = pago_bruto * 0.0287
        deduccion_sfs = pago_bruto * 0.0304
        deducciones = deduccion_afp + deduccion_sfs

        pago_neto = pago_bruto - deducciones

        datos["pago_bruto"] = pago_bruto
        datos["deducciones"] = deducciones
        datos["pago_neto"] = pago_neto

    print("Pagos calculados para todos los empleados.")
    input("\nPresione ENTER para regresar")
#------------------------------------#

#------------------------------------#
## FUNCION PRINCIPAL
def menu():
    LISTA_EMPLEADOS = {}
    OPCIONES = {
        "1": "Registrar empleado",
        "2": "Actualizar salario",
        "3": "Registrar horas",
        "4": "Calcular pago",
        "5": "Reporte: Salario mas alto",
        "6": "Reporte: Promedio salarial",
        "7": "Reporte: Empleados con horas extra",
        "8": "Exportar a .csv",
        "0": "Salir"
    }

    print("===============================")
    print("Modulo de Nomina Simple")
    print("===============================")    

    while True: # bucle infinito hasta que se eliga una opcion del menu
        print("\n=== MENÚ ===")
        for k, v in OPCIONES.items():
            print(f"{k}. {v}")
        selec = input("Elija una opción: ").strip()

        match selec:
            case "1":
                registrar_empleado(LISTA_EMPLEADOS)
            case "2":
                actualizar_salario(LISTA_EMPLEADOS)
            case "3":
                registrar_horas(LISTA_EMPLEADOS)
            case "4": 
                calcular_pagos(LISTA_EMPLEADOS)
            case "5":
                reportes.salario_mas_alto(LISTA_EMPLEADOS)
            case "6":
                reportes.promedio_salarial(LISTA_EMPLEADOS)
            case "7":
                reportes.empleados_con_horas_extra(LISTA_EMPLEADOS)
            case "8":
                reportes.exportar(LISTA_EMPLEADOS)
            case "0":
                print("Saliendo...")
                break
            case "_":
                print("Por favor ingrese una opcion valida.")
        
        limpiar_terminal()
#------------------------------------#

#------------------------------------#
# Inicia el menu en la consola
if __name__ == "__main__":
    menu()
#------------------------------------#
