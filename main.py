import os

# GRUPO 3: LYA FERRERAS, FRANK RUIZ, STEVEN CRUZ, MAXIMILIAM NOVOA.

EMPLEADOS = {}
OPCIONES = {
        "1": "Registrar empleado",
        # "2": "Actualizar salario",
        # "3": "Registrar horas",
        # "4": "Calcular pago",
        # "5": "Reporte: salario más alto",
        # "6": "Reporte: promedio salarial",
        # "7": "Reporte: EMPLEADOS con horas extra",
        "8": "Exportar datos", #this is an availaible op but it wont work without the other functions de arriba
        "0": "Salir"
    }

# Códigos de colores y formato
# NOTA: trying this out, might look weird y se puede borrar si fuera necesario y no funcione, es por estetica.
NEGRITA = '\033[1m'
ITALICA = '\033[3m'
RESET = '\033[0m'
n = 'número'

#   ------------------------------------

# funcion para menu simple
## usar un case-switch es mas eficiente que saco de elifs 🥀🥀🥀

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    while True: # bucle infinito hasta que se eliga una opcion del menu
        print("===============================")
        print("Módulo de Nómina Simple")
        print("===============================")    
        print("\n=== MENÚ ===")
        for k, v in OPCIONES.items():
            print(f"{k}. {v}")
        selec = input("Elija una opción: ").strip()

        match selec:
            case "1":
                registro_empleado(EMPLEADOS)
            #case "2":
            #    actualizar_salario(EMPLEADOS)
            #case "3":
            #    registrar_horas(EMPLEADOS)
            #case "4": 
            #    calcular_pago(EMPLEADOS)
            #case "5":
            #    reporte_salario_mas_alto(EMPLEADOS)
            #case "6":
            #    reporte_promedio_salarial(EMPLEADOS)
            #case "7":
            #    reporte_EMPLEADOS_con_horas_extras(EMPLEADOS)
            case "8":
                exportar_datos(EMPLEADOS)
            case "0":
                print("Saliendo...")
                break
            case "_":
                print("Opción inválida. Intente nuevamente.")

#------------------------------------#
# requisito extra: exportar datos a archivos
def exportar_datos(EMPLEADOS):
    with open("datos_exportados_empleados.txt", 'w') as file: # pone la lista de empleados en un archivo de texto
        file.write(str(EMPLEADOS)) # en el siguiente formato {'19549': {'nombre': 'pepe', 'salario_hora': 1200.0, 'horas_trabajadas': 0}}
#------------------------------------#


 #L: funcion para evitar que una vez el usuario introduzca un caracter que no sea igual a un numero en
   # el programa con respecto a los campos de salario/horas trabajadas el programa explote

def solicitar_numero(mensaje):
    while True:  #bucle infinito, aka, keep tryng until a valid character is introduced
        try:
            valor = float(input(mensaje).strip())
            return valor
        except ValueError:
            print(f"Error: Por favor ingrese un {NEGRITA}{n}{RESET} válido ! :(")


#   ------------------------------------



 # L: funcion para registrar a un empleado: si el empleado ya existe (dentro del diccionario)
# NO permite registrarlo nuevamente y acaba el programa SIN CAMBIOS al diccionario (**None).

def registro_empleado(EMPLEADOS):
    print("\n--- REGISTRAR EMPLEADO ---")
    id_emp = input("Ingrese el ID del empleado: ").strip() ## esto no revisa si la id esta vacia o no!! por favor arreglar :(

    if id_emp in EMPLEADOS:
        print("Error: Ya existe un empleado con ese ID.")
        return EMPLEADOS, None   # devuelve diccionario sin cambios --None

    nombre = input("Ingrese el nombre del empleado: ").strip()

    if not nombre:
        print("Error: El nombre no puede estar vacío.")

        return EMPLEADOS, None
        # no permite que se registre un empleado sin nombre/datos vacios al presionar 'enter'.

    apellido = input("Ingrese el apellido del empleado: ").strip()

    if not apellido:
        print("Error: El apellido no puede estar vacío.")
        return EMPLEADOS, None
    # no permite que se registre un empleado sin apellido/datos vacios al presionar 'enter'.


    salario_hora = solicitar_numero("Ingrese el salario por hora: ")
                   #funcion solicitar numero que no permite caracteres != nums usada.

    nuevo_registro = {
        "nombre": nombre,
        "salario_hora": salario_hora,
        "horas_trabajadas": 0
    }

    EMPLEADOS[id_emp] = nuevo_registro
    print(f"Empleado {NEGRITA}{ITALICA}{nombre} {apellido}{RESET} registrado exitosamente.")

    return EMPLEADOS, nuevo_registro
          # devuelve el diccionario actualizado con el registro creado

#corre el menu en la consola
if __name__ == "__main__":
    menu()
