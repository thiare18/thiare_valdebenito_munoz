def mostrar_medicamentos():
    print("Medicamentos almacenados:")
    for medicamento in medicamentos: # type: ignore
        print(json.dumps(medicamento, indent=4)) # type: ignore

def mostrar_laboratorios():
    print("Laboratorios almacenados:")
    for laboratorio in laboratorios: # type: ignore
        print(json.dumps(laboratorio, indent=4)) # type: ignore
