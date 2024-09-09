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
            agregar_medicamento(nombre, tipo, cantidad) # type: ignore
        elif opcion == '2':
            nombre = input("Nombre del laboratorio: ")
            ubicacion = input("Ubicación del laboratorio: ")
            agregar_laboratorio(nombre, ubicacion) # type: ignore
        elif opcion == '3':
            mostrar_medicamentos() # type: ignore
        elif opcion == '4':
            mostrar_laboratorios() # type: ignore
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()
