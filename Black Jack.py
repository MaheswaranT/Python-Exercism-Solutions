def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    elif value_two > value_one :
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    total_value = value_one + value_two
    if 'A' in [card_one, card_two]:
        return 1
    elif total_value + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    value_one = 11 if card_one == 'A' else value_of_card(card_one)
    value_two = 11 if card_two == 'A' else value_of_card(card_two)
    return value_one + value_two == 21
    

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)
    return total_value in [9, 10, 11]
