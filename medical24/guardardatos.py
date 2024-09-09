def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4) # type: ignore
