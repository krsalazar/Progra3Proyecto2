class Carro:
    def __init__(self, placa, color, linea, modelo, propietario):
        self.placa = placa
        self.color = color
        self.linea = linea
        self.modelo = modelo
        self.propietario = propietario

class Nodo:
    def __init__(self, vehiculo=None):
        self.vehiculo = vehiculo
        self.derecha = None
        self.abajo = None

class Matriz:
    def __init__(self):
        self.cabeza = Nodo()  # Nodo cabeza de la matriz

    def insertar(self, vehicle):
        # Insertar un nuevo vehículo en la matriz
        nuevo_nodo = Nodo(vehicle)

        # Insertar en la fila (placa)
        actual = self.cabeza
        while actual.abajo and actual.abajo.vehiculo.placa < vehicle.placa:
            actual = actual.abajo
        if actual.abajo is None or actual.abajo.vehiculo.placa != vehicle.placa:
            nuevo_nodo.abajo = actual.abajo
            actual.abajo = nuevo_nodo

        # Insertar en la columna (otras propiedades)
        actual = self.cabeza
        while actual.derecha and actual.derecha.vehiculo.color < vehicle.color:
            actual = actual.derecha
        if actual.derecha is None or actual.derecha.vehiculo.color != vehicle.color:
            nuevo_nodo.derecha = actual.derecha
            actual.derecha = nuevo_nodo

    def buscar(self, **kwargs):
        # Buscar vehículos según propiedades específicas
        actual = self.cabeza
        while actual:
            if actual.vehiculo:
                match = True
                for key, valor in kwargs.items():
                    if getattr(actual.vehiculo, key) != valor:
                        match = False
                        break
                if match:
                    return actual.vehiculo
            actual = actual.abajo
        return None

    def borrar(self, **kwargs):
        # Eliminar vehículos según propiedades específicas
        actual = self.cabeza
        while actual and actual.abajo:
            if actual.abajo.vehiculo:
                match = True
                for key, value in kwargs.items():
                    if getattr(actual.abajo.vehiculo, key) != value:
                        match = False
                        break
                if match:
                    actual.abajo = actual.abajo.abajo
            actual = actual.abajo

    def imprime_matriz(self):
        # Imprimir la matriz (solo para visualización)
        linea_actual = self.cabeza.abajo
        while linea_actual:
            current_node = linea_actual
            while current_node:
                if current_node.vehiculo:
                    print(f"Placa: {current_node.vehiculo.placa}, Color: {current_node.vehiculo.color}, "
                          f"Linea: {current_node.vehiculo.linea}, Modelo: {current_node.vehiculo.modelo}, "
                          f"Propietario: {current_node.vehiculo.propietario}")
                current_node = current_node.derecha
            linea_actual = linea_actual.abajo
