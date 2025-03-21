from deck import create_deck
from blackjack import calculate_hand_value

# Fonction pour distribuer des cartes aux joueurs
def deal_cards(deck, num_players=2):
    """Distribue deux cartes à chaque joueur."""
    hands = {f"Joueur {i+1}": [deck.pop(), deck.pop()] for i in range(num_players)}
    return hands

# Fonction pour jouer un tour
def player_turn(player, hand, deck, auto_action=None):
    """Permet au joueur de choisir entre Hit ou Stand, avec un mode automatique."""
    while True:
        print(f"{player}, votre main: {hand} (Score: {calculate_hand_value(hand)})")
        
        if auto_action:
            action = auto_action.pop(0) if auto_action else 'stand'
            print(f"Action automatique : {action}")
        else:
            action = input("Voulez-vous 'hit' (piocher) ou 'stand' (rester) ? ").strip().lower()
        
        if action == 'hit':
            hand.append(deck.pop())
            if calculate_hand_value(hand) > 21:
                print(f"{player} a dépassé 21 et a perdu! (Bust)")
                return False  # Le joueur a perdu
        elif action == 'stand':
            print(f"{player} décide de rester avec {hand} (Score: {calculate_hand_value(hand)})")
            return True  # Le joueur continue
        else:
            print("Choix invalide, entrez 'hit' ou 'stand'.")
