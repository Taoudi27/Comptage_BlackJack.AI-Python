def calculate_hand_value(hand):
    """Calcule la valeur d'une main en tenant compte des As."""
    value = sum(hand)
    num_aces = hand.count(11)

    # Convertir les As de 11 à 1 si nécessaire
    while value > 21 and num_aces:
        value -= 10  # Transformer un As (11) en As (1)
        num_aces -= 1

    return value
