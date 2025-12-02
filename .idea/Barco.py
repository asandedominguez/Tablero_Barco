class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0
    def recibir_impacto(self):
        self.golpes_recibidos += 1

    def esta_hundido(self):
        return self.golpes_recibidos >= self.longitud

    def mostrar_estado(self):
        print(f"Barco: {self.nombre}")
        print(f"Longitud: {self.longitud}")
        print(f"Golpes: {self.golpes_recibidos}")
        print(f"Hundido: {self.esta_hundido()}")
if __name__ == "__main__":
    submarino = Barco("Submarino", 1)
    buque = Barco("buque", 3)

    submarino.recibir_impacto()
    submarino.mostrar_estado()

    for _ in range(3):
        buque.recibir_impacto()
    buque.mostrar_estado()
