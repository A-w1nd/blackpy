import random

def get_card():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return random.choice(cards)

def calculate_score(card_list):
    score = 0
    num_aces = card_list.count("A")

    for card in card_list:
        if card == "A":
            score += 11
        elif card in ["K", "Q", "J"]:
            score += 10
        else:
            score += int(card)

    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1

    return score

def blackjack_game():
    print("Welcome to Blackjack!")

    player_cards = [get_card(), get_card()]
    computer_cards = [get_card(), get_card()]

    while True:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 21:
            print("Blackjack! You win!")
            break

        if player_score > 21:
            print("Bust! You lose.")
            break

        choice = input("Type 'hit' to get another card, or 'stand' to stop: ").lower()

        if choice == "hit":
            player_cards.append(get_card())
        elif choice == "stand":
            while computer_score < 17:
                computer_cards.append(get_card())
                computer_score = calculate_score(computer_cards)

            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

            if computer_score > 21 or (player_score <= 21 and player_score > computer_score):
                print("You win!")
            elif player_score == computer_score:
                print("Game Tied!")
            else:
                print("You lose.")
            break


    blackjack_game()
