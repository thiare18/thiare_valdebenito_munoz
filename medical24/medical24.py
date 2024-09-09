import json
import os

# Definir los nombres de los archivos
medicamentos_file = 'medicamentos.json'
laboratorios_file = 'laboratorios.json'

# Crear funciones para cargar y guardar datos
def cargar_datos(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump([], file)
        return []
    else:
        with open(filename, 'r') as file:
            return json.load(file)

def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Cargar datos iniciales
medicamentos = cargar_datos(medicamentos_file)
laboratorios = cargar_datos(laboratorios_file)

# Crear funciones para agregar medicamentos y laboratorios
def agregar_medicamento(nombre, tipo, cantidad):
    medicamento = {
        'nombre': nombre,
        'tipo': tipo,
        'cantidad': cantidad
    }
    medicamentos.append(medicamento)
    guardar_datos(medicamentos_file, medicamentos)
    print("Medicamento agregado exitosamente.")

def agregar_laboratorio(nombre, ubicacion):
    laboratorio = {
        'nombre': nombre,
        'ubicacion': ubicacion
    }
    laboratorios.append(laboratorio)
    guardar_datos(laboratorios_file, laboratorios)
    print("Laboratorio agregado exitosamente.")

# Crear funciones para mostrar información
def mostrar_medicamentos():
    print("Medicamentos almacenados:")
    for medicamento in medicamentos:
        print(json.dumps(medicamento, indent=4))

def mostrar_laboratorios():
    print("Laboratorios almacenados:")
    for laboratorio in laboratorios:
        print(json.dumps(laboratorio, indent=4))

# Crear menú principal
def menu():
    while True:
        print("\nMenu:")
        print("1. Agregar medicamento")
        print("2. Agregar laboratorio")
        print("3. Mostrar medicamentos")
        print("4. Mostrar laboratorios")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del medicamento: ")
            tipo = input("Tipo de medicamento: ")
            cantidad = input("Cantidad de medicamento: ")
            agregar_medicamento(nombre, tipo, cantidad)
        elif opcion == '2':
            nombre = input("Nombre del laboratorio: ")
            ubicacion = input("Ubicación del laboratorio: ")
            agregar_laboratorio(nombre, ubicacion)
        elif opcion == '3':
            mostrar_medicamentos()
        elif opcion == '4':
            mostrar_laboratorios()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()
