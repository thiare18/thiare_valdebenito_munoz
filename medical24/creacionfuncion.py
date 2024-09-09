def cargar_datos(filename):
    if not os.path.exists(filename): # type: ignore
        with open(filename, 'w') as file:
            json.dump([], file) # type: ignore
        return []
    else:
        with open(filename, 'r') as file:
            return json.load(file) # type: ignore
