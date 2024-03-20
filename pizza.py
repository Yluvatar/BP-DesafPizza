import ingredientes as i


class Pizza:
    precio = 10000
    tamano = 'familiar'
    pizza_valida = False

    def __init__(self):
        self.proteina = ''
        self.vegetal1 = ''
        self.vegetal2 = ''
        self.masa = ''
        self.salsa = ''

    @staticmethod
    def validar_opciones(eleccion, opciones):
        return True if eleccion in opciones else False

    def solicita_proteina(self):
        print("Proteinas Disponibles:")
        for prot in i.proteinas:
            print(f'{prot}')
        self.proteina = input('Seleccione su proteina: ')
        return True if Pizza.validar_opciones(self.proteina, i.proteinas) else False

    def solicita_vegetal(self):
        print("Vegetales Disponibles:")
        for veg in i.vegetales:
            print(f'{veg}')
        self.vegetal1 = input('Seleccione su primer vegetal: ')
        self.vegetal2 = input('Seleccione su segundo vegetal: ')
        vegetal1_val = True if Pizza.validar_opciones(self.vegetal1, i.vegetales) else False
        vegetal2_val = True if Pizza.validar_opciones(self.vegetal2, i.vegetales) else False
        return vegetal1_val and vegetal2_val

    def solicita_masa(self):
        print("Masas Disponibles:")
        for mas in i.masas:
            print(f'{mas}')
        self.masa = input('Seleccione su masa: ')
        return True if Pizza.validar_opciones(self.masa, i.masas) else False

    def solicita_salsa(self):
        print("Salsas Disponibles:")
        for salsa in i.salsas:
            print(f'{salsa}')
        self.salsa = input('Seleccione su salsa: ')
        return True if Pizza.validar_opciones(self.salsa, i.salsas) else False

    def solicita_pizza(self):
        proteina_val = self.solicita_proteina()
        vegetal_val = self.solicita_vegetal()
        masa_val = self.solicita_masa()
        salsa_val = self.solicita_salsa()

        valida = True if proteina_val and vegetal_val and masa_val and salsa_val else False
        Pizza.pizza_valida = valida

        return valida

    def pedido_pizza(self):
        return self.proteina, self.vegetal1, self.vegetal2, self.masa, self.salsa


if __name__ == '__main__':

    pizza = Pizza()

    pedido = pizza.solicita_pizza()

    if pedido:
        print("Pizza Válida")
    else:
        print("Pizza no válida")
