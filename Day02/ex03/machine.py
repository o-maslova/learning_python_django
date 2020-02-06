import random
from beverages import Tea, Chocolate, Coffee, HotBeverage, Cappuccino


class CoffeeMachine:
    amount_of_cycles = 1

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = "0.90"
        descript = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):

        def __init__(self, text):
            self.text = text

    def repair(self):
        self.amount_of_cycles = 1

    def serve(self, beverage):
        print("Cycle of usage: ", self.amount_of_cycles)
        self.amount_of_cycles += 1
        if self.amount_of_cycles > 10:
            raise self.BrokenMachineException("This coffee machine has to be repaired.")
        case = random.random() > 0.5
        if case:
            return self.EmptyCup()
        else:
            return beverage


if __name__ == '__main__':
    coffee_machine = CoffeeMachine()
    for i in range(20):
        choice = random.choice((Tea(), Coffee(), Cappuccino(), Chocolate()))
        try:
            print(coffee_machine.serve(choice), "\n")
        except coffee_machine.BrokenMachineException as err:
            print(err)
            coffee_machine.repair()
