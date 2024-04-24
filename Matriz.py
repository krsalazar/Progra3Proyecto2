class Vehicle:
    def __init__(self, plate, color, line, model, owner):
        self.plate = plate
        self.color = color
        self.line = line
        self.model = model
        self.owner = owner

class Node:
    def __init__(self, vehicle=None):
        self.vehicle = vehicle
        self.right = None
        self.down = None

class Matrix:
    def __init__(self):
        self.head = Node()  # Nodo cabeza de la matriz

    def insert(self, vehicle):
        # Insertar un nuevo vehículo en la matriz
        new_node = Node(vehicle)

        # Insertar en la fila (placa)
        current = self.head
        while current.down and current.down.vehicle.plate < vehicle.plate:
            current = current.down
        if current.down is None or current.down.vehicle.plate != vehicle.plate:
            new_node.down = current.down
            current.down = new_node

        # Insertar en la columna (otras propiedades)
        current = self.head
        while current.right and current.right.vehicle.color < vehicle.color:
            current = current.right
        if current.right is None or current.right.vehicle.color != vehicle.color:
            new_node.right = current.right
            current.right = new_node

    def search(self, **kwargs):
        # Buscar vehículos según propiedades específicas
        current = self.head
        while current:
            if current.vehicle:
                match = True
                for key, value in kwargs.items():
                    if getattr(current.vehicle, key) != value:
                        match = False
                        break
                if match:
                    return current.vehicle
            current = current.down
        return None

    def delete(self, **kwargs):
        # Eliminar vehículos según propiedades específicas
        current = self.head
        while current and current.down:
            if current.down.vehicle:
                match = True
                for key, value in kwargs.items():
                    if getattr(current.down.vehicle, key) != value:
                        match = False
                        break
                if match:
                    current.down = current.down.down
            current = current.down

    def print_matrix(self):
        # Imprimir la matriz (solo para visualización)
        current_row = self.head.down
        while current_row:
            current_node = current_row
            while current_node:
                if current_node.vehicle:
                    print(f"Plate: {current_node.vehicle.plate}, Color: {current_node.vehicle.color}, "
                          f"Line: {current_node.vehicle.line}, Model: {current_node.vehicle.model}, "
                          f"Owner: {current_node.vehicle.owner}")
                current_node = current_node.right
            current_row = current_row.down
