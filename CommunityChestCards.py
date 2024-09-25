from random import randint
from player import Player

def static_tax(player: Player):
    tax_amount = randint(5, 15)*10
    print(f"you pay {tax_amount} to the government")
    player.money -= tax_amount


def jail_free(player: Player):
    print("you get a free jail card")
    player.jainFreeCards += 1


def go_to_jail(player: Player):
    print("go to jail")
    player.position = 10
    player.inJail = True



CommunityChestCards = [
    static_tax,
    jail_free,
    go_to_jail
]


def landOnCommunityChestCards(player: Player):
    card_function: callable = CommunityChestCards[randint(0, len(CommunityChestCards)-1)]
    card_function(player)
    