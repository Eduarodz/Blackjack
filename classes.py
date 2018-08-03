import random


class Card:
    suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')

    ranks = [('Ace', 1), ('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7),
             ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 10), ('Queen', 10), ('King', 10)]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank[0]
        self.value = rank[1]

    def __str__(self):
        return f'({self.rank} of {self.suit})'


class NewDeck:

    def __init__(self, decks=1):
        self.deck = []
        for deck_num in range(0, decks):
            self.add_deck()
        self.shuffle()

    def add_deck(self):
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self, times=5):
        for i in range(0, times):
            random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop(-1)

    def __str__(self):
        my_string = ''
        for card in self.deck:
            my_string += str(card)
            my_string += '\n'
        return my_string

    def __len__(self):
        return len(self.deck)


class NewHand:

    def __init__(self):
        self.hand = []
        self.total = 0

    def __len__(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)
        self.update_total()

    def clear_hand(self):
        self.hand = []

    def got_ace(self):
        for card in self.hand:
            if card.rank != 'Ace':
                continue
            else:
                return True
        return False

    def update_total(self):
        self.total = 0
        for card in self.hand:
            self.total += card.value
        if self.got_ace() and self.total + 10 <= 21:
            self.total += 10


class BetAccount:
    def __init__(self, balance=500, min_bet=25):
        self.balance = balance
        self.min_bet = min_bet
        self.bet = 0

    @staticmethod
    def ask_bet():
        while True:
            try:
                amount = float(input('Enter bet amount: '))
            except TypeError:
                print('Input must be a number. Please try again...\n')
            else:
                return amount

    def place_bet(self):
        while True:
            amount = self.ask_bet()
            if self.min_bet <= amount <= self.balance:
                self.bet = amount
                self.balance -= amount
                break
            elif amount == 0:
                return False
            elif amount < self.min_bet:
                print('Bet must be at least 25 chips!\n')
            else:
                print('Balance not available.\n')
        return True


class NewPlayer(NewHand, BetAccount):
    def __init__(self, player=True):
        self.first = True
        self.player = player
        NewHand.__init__(self)
        BetAccount.__init__(self)

    @staticmethod
    def ask_action():
        while True:
            try:
                amount = str(input('Answer: ')).upper()
            except TypeError:
                print('Input format error. Must enter a letter. Please try again...')
            else:
                return amount

    def place_action(self):
        valid_actions = ['H', 'S', 'D']
        print('\nEnter h=Hit, s=Stand or d=Double Down\n')
        while True:
            action = self.ask_action()
            if len(action) != 1:
                print('Answer must be just one letter.\n')
            elif action not in valid_actions:
                print('Not a valid answer.\n')
            elif action == valid_actions[-1] and not self.first:
                print('Option only available as first action.\n')
            else:
                return action

    def __str__(self):
        if self.player:
            my_string = '-Player Info- [Balance: ' + str(self.balance) + '] '
            my_string += '[Bet: ' + str(self.bet) + ']\n'
        else:
            my_string = '-Dealer Info-\n'
        my_string += 'Hand Total: ' + str(self.total) + '\n'

        for card in self.hand:
            my_string += str(card)
            my_string += '  '
        return my_string + '\n'
