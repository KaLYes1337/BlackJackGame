import random

card_categories = ["♥️", "♦️️", "♣️", "♠️"]
cards_list = [
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
]
deck = [(card, category) for category in card_categories for card in cards_list]


def card_value(card):
    if card[0] in ["J", "Q", "K"]:
        return 10
    elif card[0] == "A":
        return 11
    else:
        return int(card[0])


#random.shuffle(deck)


def calculate_hand_value(hand):
    total_value = 0
    ace_counter = 0
    for card in hand:
        value = card_value(card)
        total_value += value
        if card[0] == "a":
            ace_counter += 1
        while total_value > 21 and ace_counter > 0:
            total_value -= 10
            ace_counter -= 1

    return total_value


def game_start():
    print("Welcome!")
    input_balance = float(input("State amount you want to deposit: $"))
    current_balance = input_balance
    is_playing = True
    while is_playing:
        user_input = input("(D)eal or (Q)uit: ").upper().strip()
        print("Minimum bet 5$")
        bet_amount = float(input("State your bet: $"))
        if current_balance < bet_amount:
            print("Insufficient funds!")
            break
        elif bet_amount < 5:
            print("Amount is below minimum bet!")
            break
        if user_input == "D":
            current_balance -= bet_amount
            
            player_hand = ["".join(deck.pop()), "".join(deck.pop())]
            dealer_hand = ["".join(deck.pop()), "".join(deck.pop())]

            player_total = calculate_hand_value(player_hand)
            dealer_total = calculate_hand_value(dealer_hand)

            print(
                f"Player Hand:{'  '.join([f'{card[0]}{card[1]}' for card in player_hand])}: {player_total}"
            )
            print(f"Dealer Hand:{dealer_hand[0]} , HIDDEN")
            print(f"{current_balance:.2f}\n")
            if player_total == 21:
                current_balance += bet_amount*1.5
                print("BLACK JACK! Player wins!")
                print(f"Dealer Hand:{dealer_hand[0]} , {dealer_hand[1]} | Total: {dealer_total}")
                print(f"You won ${bet_amount:.2f}")
                print(f"Balance ${current_balance:.2f}\n")
                
                next_action= input("(D)eal or (Q)uit: ").upper().strip()
                if next_action == "Q":
                    print("Thank you for playing!")
                    is_playing = False
                continue              
            action = input("Choose (H)it or (S)tand").upper()
            while action !="S":
                if action == "H":
                    player_hand.append(deck.pop())
                    player_total = calculate_hand_value(player_hand)
                    print(
                        f"Player hand {'  '.join([f'{card[0]}{card[1]}' for card in player_hand])} | {player_total}"
                    )
                elif next_action == "SPLIT":
                    player_hand.append("".join(deck.pop()))
                    player_total=calculate_hand_value(player_hand)
                    print(
                        f"Player hand {'  '.join([f'{card[0]}{card[1]}{card[2]}' for card in player_hand])} | {player_total}"
                    )
                print(f"Dealer hand {'  '.join([f'{card[0]}{card[1]}' for card in dealer_hand])} | {dealer_total}")
                    

            while dealer_total < 17:
                dealer_hand.append(deck.pop())
                dealer_total = calculate_hand_value(dealer_hand)
                print(
                    f"Dealer Hand: {'  '.join([f'{card[0]}{card[1]}' for card in dealer_hand])} | Total: {dealer_total}"
                )

            if dealer_total > 21:
                current_balance += bet_amount
                print("Player wins")
                print(f"You won ${bet_amount:.2f}")
                print(f"Balance ${current_balance:.2f}\n")
                
            elif dealer_total > player_total:

                print(f"Dealer wins! Dealer Cards!")
                print(
                    f"Dealer Hand {'  '.join([f'{card[0]}{card[1]}' for card in dealer_hand])} | {dealer_total}\n"
                )
               
                print(
                    f"Player Total {'  '.join([f'{card[0]}{card[1]}' for card in player_hand])} | {player_total}\n"
                )
                print(f"Balance ${current_balance:.2f}\n")
                

            elif player_total > dealer_total:
                bet_amount += bet_amount

                print(
                    f"Player wins! Player Cards {'  '.join([f'{card[0]}{card[1]}' for card in player_hand])} | {player_total}\n"
                )
                current_balance += bet_amount
                
                print(
                    f"Dealer Hand {'  '.join([f'{card[0]}{card[1]}' for card in dealer_hand])} | {dealer_total}"
                )
                print(f"You won ${bet_amount:.2f}\n")
                print(f"Balance ${current_balance:.2f}\n")
                
            elif player_total == dealer_total:
                current_balance+=bet_amount
                print(f"Balance ${current_balance:.2f}\n")
                print(f"Push\n")
            
        elif action == "Q":
            print("Thank you for playing!")
            is_playing = False
        else:
            print("Invalid input!")


game_start()
