from Matriz import *

if __name__ == '__main__':
    # Crear una matriz
    matriz = Matriz()

    # Insertar vehículos
    matriz.insertar(Carro("P007AMD", "Rojo", "Sedan", "2023", "Juan Perez"))
    matriz.insertar(Carro("P199HYT", "Azul", "SUV", "2022", "Ana Juarez"))
    matriz.insertar(Carro("P025KLJ", "Rojo", "Truck", "2024", "Alice Salazar"))
    matriz.insertar(Carro("M215BJT", "Negro", "Moto", "2024", "Alice Salazar"))

    # Buscar un vehículo por múltiples propiedades
    result = matriz.buscar(color="Rojo", modelo="Sedan")
    if result:
        print("Vehicle found:", result.placa, result.color, result.modelo)

    # Eliminar un vehículo por múltiples propiedades
    matriz.borrar(color="Rojo", modelo="Truck")

    # Imprimir la matriz
    matriz.imprime_matriz()

#Aun tenemos que hacer dinamica la parte de las opciones de la matriz
