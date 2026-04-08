import os 

def direccion(nombre_archivo):
    base_dir = os.path.join(os.path.dirname(__file__), "archivos")
    os.makedirs(base_dir, exist_ok=True)
    return os.path.join(base_dir, nombre_archivo)

def archivo_respuestas(operaciones):
    with open(direccion("con_respuestas.txt"), "w") as archivo:
        for op in operaciones:
            for _ in op:
                archivo.write(f"{_[0]} {_[1]} {_[2]} = {_[3]}\n")
    return "Respuestas guardadas en con_respuestas.txt"

def archivo_sin_respuestas(operaciones):
    with open(direccion("sin_respuestas.txt"), "w") as archivo:
        for op in operaciones:
            for _ in op:
                archivo.write(f"{_[0]} {_[1]} {_[2]} = \n")
    return "Operaciones guardadas en sin_respuestas.txt"
