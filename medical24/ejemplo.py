# Crear un archivo de ejemplo
with open('ejemplo.txt', 'w') as file:
    file.write("Hola Mundo, esto es una prueba de interacción para un código Python. \n Segunda parte de la prueba de interacción.")

# Leer una parte específica del archivo
with open('ejemplo.txt', 'r') as file:
    # Mover el puntero a la posición 20
    file.seek(20)
    # Leer 10 bytes desde la posición actual
    parte = file.read(10)

    print(f"Parte leída desde el byte 20 hasta el byte 30: {parte}")
