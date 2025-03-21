# Système de comptage de cartes Hi-Lo

# Attribution des valeurs aux cartes
CARD_VALUES = {
    2: 1, 3: 1, 4: 1, 5: 1, 6: 1,  # Cartes faibles (+1)
    7: 0, 8: 0, 9: 0,  # Cartes neutres (0)
    10: -1, 11: -1  # Cartes fortes (-1), 11 représente l'As
}

def update_count(card, count):
    """Met à jour le compte courant en fonction de la carte tirée."""
    return count + CARD_VALUES.get(card, 0)

def calculate_true_count(count, decks_remaining):
    """Calcule le True Count en divisant le compte courant par le nombre de paquets restants."""
    if decks_remaining == 0:
        return count  # Évite la division par zéro
    return round(count / decks_remaining)

def count_cards(cards, count):
    """Met à jour le comptage pour plusieurs cartes."""
    for card in cards:
        count = update_count(card, count)
    return count
