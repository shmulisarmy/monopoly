from random import randint

def roll_dice():
    dice_one = randint(1, 6)
    dice_two = randint(1, 6)

    return {
        "amount": dice_one + dice_two,
        "is_double": dice_one == dice_two
    }

