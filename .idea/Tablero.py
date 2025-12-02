class Tablero:
    def __init__(self, tamano):
        self.dimensiones = (tamano, tamano)
        self.casillas = [[0 for _ in range(tamano)] for _ in range(tamano)]
    def mostrar_tablero(self):
        for fila in self.casillas:
            print(fila)
if __name__ == "__main__":
    tablero = Tablero(5)
    tablero.mostrar_tablero()
