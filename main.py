print("===============================")
print("Módulo de Nómina Simple")
# GRUPO 3: LYA FERRERAS, FRANK RUIZ, STEVEN CRUZ, MAXIMILIAM NOVOA.
print("===============================")


# Códigos de colores y formato
# NOTA: trying this out, might look weird y se puede borrar si fuera necesario y no funcione, es por estetica.
NEGRITA = '\033[1m'
ITALICA = '\033[3m'
RESET = '\033[0m'
n = 'número'

#   ------------------------------------

 # funcion para menu simple
  #nota: los elif's y textos con "#" no han sido funciones creadas en el programa todavia. una vez creadas
  # se le quitaran los hashtags.

def menu():
    empleados = {}
    opciones = {
        "1": "Registrar empleado",
        # "2": "Actualizar salario",
        # "3": "Registrar horas",
        # "4": "Calcular pago",
        # "5": "Reporte: salario más alto",
        # "6": "Reporte: promedio salarial",
        # "7": "Reporte: empleados con horas extra",
        "0": "Salir"
    }

    # bucle infinito hasta que se eliga una opcion del menu
    while True:
        print("\n=== MENÚ ===")
        for k, v in opciones.items():
            print(f"{k}. {v}")
        op = input("Elija una opción: ").strip()

        if op == "1":
           empleados, _ = registro_empleado(empleados)
        # elif op == "2":
        #     empleados, _ = actualizar_salario(empleados)
        # elif op == "3":
        #     empleados, _ = registrar_horas(empleados)
        # elif op == "4":
        #     empleados, _ = calcular_pago(empleados)
        # elif op == "5":
        #     _ = reporte_salario_mas_alto(empleados)
        # elif op == "6":
        #     _ = reporte_promedio_salarial(empleados)
        # elif op == "7":
        #     _ = reporte_empleados_con_horas_extras(empleados)
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



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

def registro_empleado(empleados):
    print("\n--- REGISTRAR EMPLEADO ---")
    id_emp = input("Ingrese el ID del empleado: ").strip()

    if id_emp in empleados:
        print("Error: Ya existe un empleado con ese ID.")
        return empleados, None   # devuelve diccionario sin cambios --None

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return empleados, None
        #no permite que se registre un empleado sin nombre/datos vacios al presionar 'enter'.

    nombre = input("Ingrese el nombre del empleado: ").strip()
    salario_hora = solicitar_numero("Ingrese el salario por hora: ")
                   #funcion solicitar numero que no permite caracteres != nums usada.

    nuevo_registro = {
        "nombre": nombre,
        "salario_hora": salario_hora,
        "horas_trabajadas": 0
    }

    empleados[id_emp] = nuevo_registro
    print(f"Empleado {NEGRITA}{ITALICA}{nombre}{RESET} registrado exitosamente.")

    return empleados, nuevo_registro
          # devuelve el diccionario actualizado con el registro creado

