from random import choice
CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Player:
    def __init__(self):
        self.cards = []
        self.aces = 0
        self.current_score = 0

    def add_to_current_score(self, card):
        if card in ['J', 'Q', 'K']:
            self.current_score += 10
            return
        if card != 'A':
            self.current_score += int(card)
            return
        if self.current_score < 11:
            self.current_score += 11
            return
        self.current_score += 1
        return

    def get_card(self, target=None):
        card = choice(CARDS)
        self.cards.append(card)
        if card == 'A':
            self.aces += 1
        self.add_to_current_score(card)

    def show_cards(self, is_first_card_only=False):
        if not is_first_card_only:
            return ", ".join(self.cards)
        return self.cards[0]

    def show_last_card(self):
        return self.cards[-1]

    def is_blackjack(self):
        if len(self.cards) != 2:
            return False
        if self.aces == 0:
            return False
        if self.aces == 2:
            return True
        if self.aces == 1:
            has_ten = False
            for card in self.cards:
                if card not in ['10', 'J', 'Q', 'K']:
                    continue
                has_ten = True
            return True if has_ten else False

