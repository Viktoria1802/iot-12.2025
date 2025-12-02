from enum import Enum

class CandyType(Enum):
    """
    Enum representing different types of candies.
    """
    BAR = "Bar"
    BUTTON = "Button"
    POPCORN = "Popcorn"
    GUM = "Gum"
    CHOCOLATE = "Chocolate"
    LOLLYPOP = "Lollypop"

class Product:
    """
    Product class representing a generic product.
    """
    def __init__(self, name, price):
        """
        initialize product whith name and price
        """
        self._price = price
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

class Candy(Product):
    """
    Candy class inhering ftom Product class.
    """
    def __init__(self, name = str, mass_in_grams = float, amount = int, price = float, candy_type = CandyType):
        """
        Initialize a Candy object with name, mass in grams, amount, price, and candy type.
        """
        super().__init__(name, price)
        self._mass_in_grams = mass_in_grams
        self._amount = amount
        self._candy_type = candy_type
    
    def __del__(self):
        """
        Destructor for Candy object.
        """
        print(f"Candy objekt {self.name} is being deleted.")

    @property
    def mass_in_grams(self):
        return self._mass_in_grams

    @mass_in_grams.setter
    def mass_in_grams(self, mass_in_grams):
        if value < 0:
            raise ValueError("Mass in grams cannot be negative.")
        self._mass_in_grams = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if new_amount < 0:
            raise ValueError("Amount cannot be negative.")
        self._amount = new_amount

    @property
    def candy_type(self):
        return self._candy_type

    def total_cost(self):
        return self.price * self.amount

    def total_mass_kg(self):
        return (self.mass_in_grams * self.amount) / 1000.0

    def ate(self):
        if self.amount > 2:
            return("You are on a diet!")
        return ("What delicious candies!")

    def __str__(self):
        return (f'Candy -  name:"{self._name}" \n' +\
            f'Candy.type:"{self._candy_type}" \n' +\
            f'Mass:"{self._mass_in_grams}g" \n' +\
            f'Amont:"{self._amount}" \n' +\
            f'Prise:$"{self._price}"')
    def __repr__ (self):
        return(f'Candy -  name:"{self._name}", Candy.type:{self._candy_type}, '
            f'Mass:{self._mass_in_grams}g Amont:{self._amount}, Prise:${self._price}')

class Dinner:
    """
    Dinner class representing a dinner event with candies.
    """
    def __init__(self, day, time): 
        self._day = day
        self._time = time
        self.candies = []
        
    @property
    def day(self):
        return self._day

    @property
    def time(self):
        return self._time
    def add_candy(self, candy: Candy):
        self.candies.append(candy)
    
    def display_dinner(self):
        print(f"Dinner on {self.day} at {self.time}")
        for candy in self.candies:
            print(candy)

    def findTheMostExpensiveCandies(self):
        sorted_candies = sorted(self.candies, key=lambda c: c.price, reverse=True)
        return sorted_candies[:3]

def main():
    
    candy1 = Candy("ChocoBar", 50, 30, 2.5, CandyType.BAR)
    candy2 = Candy("SweetPop", 10, 300, 0.5, CandyType.POPCORN)
    candy3 = Candy("GumBall", 5, 500, 0.2, CandyType.GUM)
    candy4 = Candy("Caramel", 20, 50, 1.5, CandyType.BUTTON)
    
    dinner = Dinner("Monday", "18:00")
    
    dinner.add_candy(candy1)
    dinner.add_candy(candy2)
    dinner.add_candy(candy3)
    dinner.add_candy(candy4)
   
    dinner.display_dinner()
    
    print(candy2.ate())
    
    expensive_candies = dinner.findTheMostExpensiveCandies()
    print("\nTop 3 most expensive candies:")
    for candy in expensive_candies:
        print(candy)

if __name__ == "__main__":
    main()

