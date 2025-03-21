from blackjack import calculate_hand_value

def bot_decision(hand, dealer_card, true_count):
    """Le bot prend des décisions basées sur le True Count et la carte du croupier."""
    hand_value = calculate_hand_value(hand)
    
    # Si la main est forte (17+), on reste toujours
    if hand_value >= 17:
        return "stand"
    
    # Si le True Count est élevé et que la main est faible, on tente un hit
    if true_count > 2 and hand_value < 16:
        return "hit"
    
    # Stratégie simple : si le croupier a une carte forte (7+), on prend plus de risques
    if dealer_card >= 7:
        return "hit" if hand_value < 17 else "stand"
    else:
        return "stand"
