from utils import roll_dice
from player import Player
from property import positions, Property


class Game:
    def __init__(self, players: list[Player], properties: list[Property], positions: dict[int, Property|str]):
        self.players = []
        self.properties = []
        self.current_player = None
        self.current_property = None
        self.current_turn = 0
        self.positions: dict[int, Property|str] = positions


    def turn(self, current_player):
        self.current_player = current_player
        dice_roll_iterataion = 0

        while dice_roll_iterataion < 3:
            dice_roll_iterataion += 1
            rolled_dice = roll_dice()

            if not rolled_dice["is_double"]:
                return
            
            current_player.move(rolled_dice["amount"])
            

        



    def infinite_player_cyle(self):
        index: int = 0

        while True:
            yield self.players[index]
            index += 1
            if index >= len(self.players):
                index = 0

    def auction(self, property):
        auction_amount: int = 100
        current_highest_bidder = None
        for player in self.infinite_player_cyle():
            if not input(f"Would you like to make a bid of higher than {auction_amount} on {property.name}? (y/n) ").lower() == "y":
                continue

            bid_amount = int(input("How much would you like to bid? "))

            if bid_amount < auction_amount:
                print("thats too low")
                continue

            if not player.canPay(bid_amount):
                print("you cant afford that")
                continue

            current_highest_bidder = player
            auction_amount = bid_amount


        if current_highest_bidder:
            current_highest_bidder.buy_property(property)

        else:
            print("no one bids")
                


mediterranean_avenue = Property("Mediterranean Avenue", 60, 2, "Brown", 1)
baltic_avenue = Property("Baltic Avenue", 60, 4, "Brown", 3)
reading_railroad = Property("Reading Railroad", 200, 25, "Railroad", 5)
oriental_avenue = Property("Oriental Avenue", 100, 6, "Light Blue", 6)
vermont_avenue = Property("Vermont Avenue", 100, 6, "Light Blue", 8)
connecticut_avenue = Property("Connecticut Avenue", 120, 8, "Light Blue", 9)
st_charles_place = Property("St. Charles Place", 140, 10, "Pink", 11)
electric_company = Property("Electric Company", 150, 0, "Utility", 12)
states_avenue = Property("States Avenue", 140, 10, "Pink", 13)
virginia_avenue = Property("Virginia Avenue", 160, 12, "Pink", 14)
pennsylvania_railroad = Property("Pennsylvania Railroad", 200, 25, "Railroad", 15)
st_james_place = Property("St. James Place", 180, 14, "Orange", 16)
tennessee_avenue = Property("Tennessee Avenue", 180, 14, "Orange", 18)
new_york_avenue = Property("New York Avenue", 200, 16, "Orange", 19)
kentucky_avenue = Property("Kentucky Avenue", 220, 18, "Red", 21)
indiana_avenue = Property("Indiana Avenue", 220, 18, "Red", 23)
illinois_avenue = Property("Illinois Avenue", 240, 20, "Red", 24)
b_and_o_railroad = Property("B. & O. Railroad", 200, 25, "Railroad", 25)
atlantic_avenue = Property("Atlantic Avenue", 260, 22, "Yellow", 26)
ventnor_avenue = Property("Ventnor Avenue", 260, 22, "Yellow", 27)
water_works = Property("Water Works", 150, 0, "Utility", 28)
marvin_gardens = Property("Marvin Gardens", 280, 24, "Yellow", 29)
pacific_avenue = Property("Pacific Avenue", 300, 26, "Green", 31)
north_carolina_avenue = Property("North Carolina Avenue", 300, 26, "Green", 32)
pennsylvania_avenue = Property("Pennsylvania Avenue", 320, 28, "Green", 34)
short_line = Property("Short Line", 200, 25, "Railroad", 35)
park_place = Property("Park Place", 350, 35, "Dark Blue", 37)
boardwalk = Property("Boardwalk", 400, 50, "Dark Blue", 39)

# Create the positions dictionary
positions: dict[int, Property|str] = {
    0: "GO",
    1: mediterranean_avenue,
    2: "Community Chest",
    3: baltic_avenue,
    4: "Income Tax",
    5: reading_railroad,
    6: oriental_avenue,
    7: "Chance",
    8: vermont_avenue,
    9: connecticut_avenue,
    10: "Jail",
    11: st_charles_place,
    12: electric_company,
    13: states_avenue,
    14: virginia_avenue,
    15: pennsylvania_railroad,
    16: st_james_place,
    17: "Community Chest",
    18: tennessee_avenue,
    19: new_york_avenue,
    20: "Free Parking",
    21: kentucky_avenue,
    22: "Chance",
    23: indiana_avenue,
    24: illinois_avenue,
    25: b_and_o_railroad,
    26: atlantic_avenue,
    27: ventnor_avenue,
    28: water_works,
    29: marvin_gardens,
    30: "Go To Jail",
    31: pacific_avenue,
    32: north_carolina_avenue,
    33: "Community Chest",
    34: pennsylvania_avenue,
    35: short_line,
    36: "Chance",
    37: park_place,
    38: "Luxury Tax",
    39: boardwalk
}


from CommunityChestCards import landOnCommunityChestCards

def landOnGo(player):
    player.money += 200


def landOnGoToJail(player):
    player.position = 10
    player.inJail = True



def LuxuryTax(player: Player):
    tax_amount = 75
    print(f"you pay {tax_amount} to the government")
    player.money -= tax_amount


onLandFunctions = {
    "Go": landOnGo,
    "Go To Jail": landOnGoToJail,
    "Chance": landOnCommunityChestCards,
    "Community Chest": landOnCommunityChestCards,
    "Luxury Tax": LuxuryTax,
    "Income Tax": LuxuryTax,
}

    


