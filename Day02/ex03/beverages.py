class HotBeverage:
    name = "hot beverage"
    price = "0.30"
    descript = "Just some hot water in a cup."

    def description(self):
        return self.descript

    def __str__(self):
        return "name : {name}\n" \
               "price : {price}\n" \
               "description: {description}".format(name=self.name,
                                                   price=self.price,
                                                   description=self.description())


class Coffee(HotBeverage):
    name = "coffee"
    price = "0.40"
    descript = "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"
    price = 0.30
    descript = "Just some hot water in a cup."


class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    descript = "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    descript = "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__':
    beverage = HotBeverage()
    print(beverage, "\n")
    coffee = Coffee()
    print(coffee, "\n")
    tea = Tea()
    print(tea, "\n")
    chocolate = Chocolate()
    print(chocolate, "\n")
    cappuccino = Cappuccino()
    print(cappuccino, "\n")
