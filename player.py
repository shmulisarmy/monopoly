from property import positions

class Player:
    def __init__(self, name, position, money, properties, houses, hotels):
        self.name = name
        self.position = position
        self.money = money
        self.properties = properties


    def canPay(self, amount: int):
        if self.money >= amount:
            return True
        potential_cash_to_pay = self.money
        for property in self.properties:
            potential_cash_to_pay += property.get_mortgage_amount()

        if potential_cash_to_pay >= amount:
            return True
        return False
    

    def move(self, amount: int):
        from game import positions
        self.position = (self.position + amount) % 40

        position = positions[self.position]

        if isinstance(position, property):
            position.onLand(self)
            return
        
        position_on_land_func = positions.get(position)

        if position_on_land_func:
            position_on_land_func(self)
        
    
