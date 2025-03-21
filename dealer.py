from blackjack import calculate_hand_value

# Fonction pour le tour du croupier
def dealer_turn(deck):
    """Le croupier pioche des cartes jusqu'à avoir au moins 17 points."""
    hand = [deck.pop(), deck.pop()]
    print(f"Croupier commence avec : {hand} (Score: {calculate_hand_value(hand)})")
    
    while calculate_hand_value(hand) < 17:
        hand.append(deck.pop())
        print(f"Croupier pioche : {hand} (Score: {calculate_hand_value(hand)})")
    
    if calculate_hand_value(hand) > 21:
        print("Croupier a dépassé 21 et perd! (Bust)")
    else:
        print(f"Croupier reste avec : {hand} (Score: {calculate_hand_value(hand)})")
    
    return hand
