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
        return empleados, None   # devuelve diccionario sin cambios y None

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