def calculate_bet(true_count, base_bet=10, max_bet=100):
    """Calcule la mise en fonction du True Count."""
    if true_count <= 0:
        return base_bet  # Si le comptage est bas, on mise le minimum
    
    # Ajuster la mise en fonction du True Count (ex: 10 * True Count, jusqu'à max_bet)
    bet = base_bet * (1 + true_count)
    return min(bet, max_bet)  # Ne pas dépasser la mise maximale
