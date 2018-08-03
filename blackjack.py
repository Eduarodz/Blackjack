from blackjack_classes import*
from blackjack_functions import*

deck = NewDeck(8)

player = NewPlayer()
dealer = NewPlayer(False)

while True:
    balance_flag = check_balance(player)
    display_game(player, dealer)
    if balance_flag:
        print('Your balance was low. We added '+str(player.min_bet*3)+' chips...\n')
    bet = player.place_bet()
    if not bet:
        break
    set_table(player, dealer, deck)
    player.first = True
    play = True
    while play:
        selection = player.place_action()
        if selection == 'H':
            play = hit(player, dealer, deck)
            player.first = False
        elif selection == 'S':
            play = stand(player, dealer, deck)
        elif selection == 'D':
            play = double_down(player, dealer, deck)
        else:
            break
    clear_hands(player, dealer)
