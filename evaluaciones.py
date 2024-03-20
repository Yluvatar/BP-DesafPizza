import ingredientes as i
from pizza import Pizza

print(f"Tamaño de la pizza {Pizza.tamano}")
print(f"Valor de la pizza es: ${Pizza.precio}")

print(f"Salsa de tomate {'existe' if 'salsa de tomate' in i.salsas else 'no existe'} en la lista")

pizza = Pizza()

pedido = pizza.solicita_pizza()

proteina, vegetal1, vegetal2, masa, salsa = pizza.pedido_pizza()

if pedido:
    print("\n Pizza válida")
    print("\n Su Pedido es:")
    print(f"Proteina: {proteina}")
    print(f"Su primer vegetal es: {vegetal1}")
    print(f"Su segundo vegetal es: {vegetal2}")
    print(f"Su masa es: {masa}")
    print(f"Su salsa es: {salsa}\n")
else:
    print("Pizza no válida")

print(f"La pizza {'es Válida' if Pizza.pizza_valida else 'no es Válida'}")
