from Matriz import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Crear una matriz
    matrix = Matrix()

    # Insertar vehículos
    matrix.insert(Vehicle("ABC123", "Red", "Sedan", "2023", "John Doe"))
    matrix.insert(Vehicle("XYZ789", "Blue", "SUV", "2022", "Jane Smith"))
    matrix.insert(Vehicle("DEF456", "Red", "Truck", "2024", "Alice Johnson"))

    # Buscar un vehículo por múltiples propiedades
    result = matrix.search(color="Red", model="Sedan")
    if result:
        print("Vehicle found:", result.plate, result.color, result.model)

    # Eliminar un vehículo por múltiples propiedades
    matrix.delete(color="Red", model="Truck")

    # Imprimir la matriz
    matrix.print_matrix()


