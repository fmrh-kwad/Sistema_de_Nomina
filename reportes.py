#------------------------------------#
def salario_mas_alto(empleados):
    print("\n===============================")
    print("Reporte: salario más alto")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return

    # Usamos el pago_neto; si aún es 0, se verá reflejado
    empleado_max = max(empleados.items(), key=lambda x: x[1]["pago_neto"])
    emp_id, datos = empleado_max

    print(f"Empleado con mayor pago neto:")
    print(f"ID: {emp_id}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Pago bruto: {datos['pago_bruto']:.2f}")
    print(f"Deducciones: {datos['deducciones']:.2f}")
    print(f"Pago neto: {datos['pago_neto']:.2f}")

    input("\nPresione ENTER para regresar")
#------------------------------------#

#------------------------------------#
def promedio_salarial(empleados):
    print("\n===============================")
    print("Reporte: promedio salarial (pago neto)")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return

    total = sum(d["pago_neto"] for d in empleados.values())
    promedio = total / len(empleados)
    print(f"Promedio de pago neto: {promedio:.2f}")

    input("\nPresione ENTER para regresar")
#------------------------------------#

#------------------------------------#
def empleados_con_horas_extra(empleados):
    print("\n===============================")
    print("Reporte: empleados con horas extra")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return

    encontrados = False
    for emp_id, datos in empleados.items():
        if datos["horas_extra"] > 0:
            encontrados = True
            print(f"ID: {emp_id} | Nombre: {datos['nombre']} | "
                  f"Horas extra: {datos['horas_extra']} | Pago neto: {datos['pago_neto']:.2f}")

    if not encontrados:
        print("Ningún empleado tiene horas extra registradas.")
    
    input("\nPresione ENTER para regresar")
#------------------------------------#

#------------------------------------#
def exportar(empleados):
    from datetime import date
    import csv
    print("\n===============================")
    print("Exportar datos a archivo CSV")
    print("===============================")
    if not empleados:
        print("No hay empleados registrados.")
        input("Presione ENTER para regresar")
        return

    nombre_archivo = "Nomina_De_Empleados_" + date.today().strftime("%Y-%m-%d") + ".csv"

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as f:
        campos = [
            "id", "nombre", "salario_hora",
            "horas_trabajadas", "horas_extra",
            "pago_bruto", "deducciones", "pago_neto"
        ]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()

        for emp_id, datos in empleados.items():
            fila = {
                "id": emp_id,
                "nombre": datos["nombre"],
                "salario_hora": datos["salario_hora"],
                "horas_trabajadas": datos["horas_trabajadas"],
                "horas_extra": datos["horas_extra"],
                "pago_bruto": datos["pago_bruto"],
                "deducciones": datos["deducciones"],
                "pago_neto": datos["pago_neto"],
            }
            writer.writerow(fila)

    print(f"\nDatos exportados correctamente a {nombre_archivo}")
    input("\nPresione ENTER para regresar")
#------------------------------------#