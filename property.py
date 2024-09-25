from utils import roll_dice
from player import Player
from game import Game
from collections import defaultdict

class Property:
    all_instances_by_position = {}
    all_instances_by_name = {}
    sets = defaultdict(list)
    def __init__(self, name, price, rent, set_part_of, position):
        self.rent: int = rent
        self.name: str = name
        self.price: int = price
        self.houses: int = 0
        self.set_part_of = set_part_of
        self.rent_override = None
        self.position = position
        self.ismortgaged = False
        self.owner = None

        self.all_instances_by_position[position] = self
        self.all_instances_by_name[name] = self
        self.sets[set_part_of].append(self)



    def get_rent(self):
        if self.rent_override:
            return self.rent_override()
        
        if self.houses == 0:
            if self.is_part_of_set():
                return self.rent*2
            return self.rent
        if self.houses == 1:
            return self.rent*5
        if self.houses == 2:
            return self.rent*10
        if self.houses == 3:
            return self.rent*20
        if self.houses == 4:
            return self.rent*30
        if self.houses == 5:
            return self.rent*40
        

    def onLand(self, player):
        if not self.owner:
            if player.canPay(self) and input(f"Would you like to buy {self.name} for {self.price}? (y/n) ").lower() == "y":
                player.buy_property(self)
                return
            else:
                Game.auction(self)

            return

        if self.ismortgaged:
            print(f"{self.name} is mortgaged. you dont have to pay rent.")
            return
        
        if self.owner == player:
            print(f"{self.name} is owned by you. you dont have to pay rent.")
            return

        self.collect(unfortionate_player=player)




    def collect(self, unfortionate_player=None):
        if unfortionate_player.canPay(self.get_rent()):
            unfortionate_player.pay(self.get_rent())
        else:
            unfortionate_player.lose(lost_to=self.owner)

    def is_part_of_set(self):
        return all(prop.owner == self.owner for prop in Property.sets[self.set_part_of])
            
    
    def get_mortgage_amount(self) -> int:
        return self.price // 2
    








