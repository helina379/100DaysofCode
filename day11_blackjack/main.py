import random
import art
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = []
computer_card = []
for i in range(0, 2):
    player_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))

# computer_card.append(random.choice(cards))


def sum_cards(card_deck):
    sum_deck = 0
    for j in range(0, len(card_deck)):
        sum_deck += card_deck[j]
    # print(sum_deck)
    return sum_deck


# another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

def card_adder(player_card):
        player_card.append(random.choice(cards))
        print(f"Your cards: {player_card}, current score : {sum_cards(player_card)}") #might have to use print??
        print(f"Computer's first card: {computer_card[0]}")

def computer_adder(computer_card):
    if sum_cards(computer_card) < 16:
        computer_card.append(random.choice(cards))
        computer_adder(computer_card)
    return computer_card


def asker(player_card):
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another_card == "y" and sum_cards(player_card) < 21:
        card_adder(player_card)
        if sum_cards(player_card) >21:
            print("Busted")
            print("You lose")
        else:
            asker(player_card)

    elif sum_cards(player_card) >21:
        print("Busted")
        print("You lose")

    elif another_card == "n":
        print(f"Your final hand: {player_card}, final score : {sum_cards(player_card)}")
        print(f"Computer's final hand: {computer_card}, final score : {sum_cards(computer_card)}")
        # if sum_cards(player_card) > 21:
        #     print("Busted")
        #     print("You lose")
        if sum_cards(player_card) < sum_cards(computer_card):
            print("You lose")
        elif sum_cards(player_card) == sum_cards(computer_card):
            print("Draw")
        elif sum_cards(player_card) > sum_cards(computer_card):
            print("You win")



print(f"Your cards: {player_card}, current score : {player_card[0]+player_card[1]}")
print(f"Computer's first card: {computer_card[0]}")
asker(player_card)


# while another_card == "y":
#     player_card.append(cards)
#     print(f"Your cards: {player_card}, current score : {sum_cards(player_card)}")
#     print(f"Computer's first card: {computer_card[0]}")
