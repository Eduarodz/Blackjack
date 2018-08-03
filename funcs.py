import os


def set_table(player, dealer, deck):
    player.add_card(deck.pop_card())
    dealer.add_card(deck.pop_card())
    player.add_card(deck.pop_card())
    display_game(player, dealer)
    if player.total == 21:
        stand(player, dealer, deck)


def choose_winner(player, dealer):
    if player.total <= 21 and (player.total > dealer.total or dealer.total > 21):
        player.balance += player.bet*2
        player.bet = 0
        display_game(player, dealer)
        input('\nPlayer Wins!')
        player.total, dealer.total = (0, 0)

    elif player.total == dealer.total:
        player.balance += player.bet
        player.bet = 0
        display_game(player, dealer)
        input('\nPush!')
        player.total, dealer.total = (0, 0)
    else:
        player.bet = 0
        display_game(player, dealer)
        input('\nPlayer loses...')
        player.total, dealer.total = (0, 0)


def stand(player, dealer, deck):
    while dealer.total <= 17 and dealer.total < player.total:
        dealer.add_card(deck.pop_card())
        display_game(player, dealer)
        if player.total > 21:
            break
    choose_winner(player, dealer)
    return False


def hit(player, dealer,  deck):
    player.add_card(deck.pop_card())
    display_game(player, dealer)
    if player.total >= 21:
        play = stand(player, dealer, deck)
        return play
    return True


def double_down(player, dealer, deck):
    if player.balance >= player.bet:
        player.balance -= player.bet
        player.bet *= 2
        hit(player, dealer, deck)
        play = stand(player, dealer, deck)
        return play
    else:
        print('Balance not available...')
        return True


def clear_hands(player, dealer):
    player.clear_hand()
    dealer.clear_hand()


def display_game(player, dealer, clear=True):
    if clear:
        os.system('cls')
        print('\n   BLACKJACK    (Bet 0 chips to exit)\n')
    print(player)
    print(dealer)


def check_balance(player):
    if player.balance < player.min_bet:
        player.balance += player.min_bet*3
        return True
    else:
        return False
