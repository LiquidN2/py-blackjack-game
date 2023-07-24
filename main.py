from art import LOGO
from player import Player


if __name__ == "__main__":
    print(LOGO)
    print("Welcome to Blackjack Game!")
    while True:
        play_game = input("Do you want to play a game of Blackjack? (Answer: y/n) ").strip()
        if play_game != "y":
            break

        player_me = Player()
        computer = Player()

        player_me.get_card()
        computer.get_card()
        player_me.get_card()
        computer.get_card()

        # Check for Blackjack
        if player_me.is_blackjack() and not computer.is_blackjack():
            print("Congratulations! You have Blackjack! You win!")
            continue

        if not player_me.is_blackjack() and computer.is_blackjack():
            print("Sorry, The computer has Blackjack! You lose!")
            continue

        print(f"Your cards: [{player_me.show_cards()}]")
        print(f"Your current score is: {player_me.current_score}")
        print(f"Computer's cards: [{computer.show_cards(is_first_card_only=True)}, *]")

        while True:
            another_card = input("Would you like to another card? (Answer: y/n) ").strip()
            if another_card != 'y' or player_me.current_score > 21 or len(player_me.cards) >= 5:
                break

            player_me.get_card()
            print(f"You've drawn a {player_me.show_last_card()}")
            print(f"Your current score is: {player_me.current_score}")

            if computer.current_score < 21 and len(computer.cards) < 5:
                computer.get_card()

        while True:
            if computer.current_score >= 21 or len(computer.cards) >= 5:
                break
            computer.get_card()

        print(f"The computer score is {computer.current_score}")
        if player_me.current_score > computer.current_score:
            print("Congratulations! You win!")
            continue

        if player_me.current_score < computer.current_score:
            print("Sorry, the computer wins")
            continue
