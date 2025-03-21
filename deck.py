import random

# Définition des cartes (valeurs uniquement, les couleurs n'ont pas d'importance au blackjack)
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 11 représente l'As

def create_deck():
    """Crée un deck de 52 cartes et le mélange."""
    deck = CARDS * 4  # Un deck standard a 4 fois chaque carte
    random.shuffle(deck)  # Mélange du deck
    return deck
