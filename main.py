import random
from deck import create_deck
from game import deal_cards, player_turn
from blackjack import calculate_hand_value
from dealer import dealer_turn
from counting import count_cards, calculate_true_count
from betting import calculate_bet
import bot_player

# Création du deck
deck = create_deck()

total_decks = 1  # On suppose un seul paquet pour l'instant
cards_remaining = len(deck)
count = 0  # Initialisation du comptage

print("\n--- DÉBUT DE LA PARTIE ---\n")

# Distribution des cartes aux joueurs
players_hands = deal_cards(deck)

# Mise à jour du comptage avec les cartes distribuées
for hand in players_hands.values():
    count = count_cards(hand, count)

# Ajout d'un bot joueur
auto_actions = {}
for player in players_hands.keys():
    auto_actions[player] = []

# Tour de chaque joueur
for player, hand in players_hands.items():
    decks_remaining = max(1, (cards_remaining // 52))  # Évite la division par zéro
    true_count = calculate_true_count(count, decks_remaining)
    bet = calculate_bet(true_count)
    print(f"\n--- Tour de {player} ---")
    print(f"Mise suggérée: {bet} chips (True Count: {true_count})")
    
    # Simuler le jeu du bot en affichant chaque action en temps réel
    while True:
        dealer_card = deck[-1]  # On suppose que la carte visible du croupier est la dernière du deck
        decision = bot_player.bot_decision(hand, dealer_card, true_count)
        print(f"{player} décide de {decision}")
        
        if decision == "hit":
            card_drawn = deck.pop()
            print(f"{player} pioche un {card_drawn}")
            hand.append(card_drawn)
            count = count_cards([card_drawn], count)
            
            if calculate_hand_value(hand) > 21:
                print(f"{player} a busté et perd.")
                break
        else:
            print(f"{player} reste avec {hand} (Score: {calculate_hand_value(hand)})")
            break

# Tour du croupier
print("\n--- Tour du Croupier ---")
dealer_hand = dealer_turn(deck)
count = count_cards(dealer_hand, count)

# Mise à jour du True Count
decks_remaining = max(1, (cards_remaining // 52))
true_count = calculate_true_count(count, decks_remaining)

print("\n--- RÉSULTATS ---")
print(f"Comptage Hi-Lo: {count}")
print(f"True Count: {true_count}")

# Comparaison des scores
dealer_score = calculate_hand_value(dealer_hand)
for player, hand in players_hands.items():
    player_score = calculate_hand_value(hand)
    print(f"\n{player}:")
    print(f"  - Main: {hand}")
    print(f"  - Score: {player_score}")
    if player_score > 21:
        print(f"  {player} a busté et perd.")
    elif dealer_score > 21 or player_score > dealer_score:
        print(f"  {player} gagne contre le croupier!")
    elif player_score < dealer_score:
        print(f"  {player} perd contre le croupier.")
    else:
        print(f"  {player} fait égalité avec le croupier.")

print("\n--- FIN DE LA PARTIE ---\n")
