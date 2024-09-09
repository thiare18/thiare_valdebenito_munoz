def agregar_medicamento(nombre, tipo, cantidad):
    medicamento = {
        'nombre': nombre,
        'tipo': tipo,
        'cantidad': cantidad
    }
    medicamentos.append(medicamento) # type: ignore
    guardar_datos(medicamentos_file, medicamentos) # type: ignore
    print("Medicamento agregado exitosamente.")

def agregar_laboratorio(nombre, ubicacion):
    laboratorio = {
        'nombre': nombre,
        'ubicacion': ubicacion
    }
    laboratorios.append(laboratorio) # type: ignore
    guardar_datos(laboratorios_file, laboratorios) # type: ignore
    print("Laboratorio agregado exitosamente.")
