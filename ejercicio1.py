class Coche:
    def __init__(self, marca, modelo):
        # Asigna la marca proporcionada al atributo 'marca'
        # Asigna el modelo proporcionado al atributo 'modelo'
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return f"Conduciendo el {self.marca} {self.modelo}"

