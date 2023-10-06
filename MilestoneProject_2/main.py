import random
x = ''
dealer = []
player = []
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}

playing = True
cont = True
total = 100
flag = ''
add_card = ''


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.sum1 = 0
        self.sum2 = 0
        self.dealer = []
        self.player = []
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.deck.append(created_card)

    def __str__(self):
        deck_string = ''
        for card in self.deck:
            deck_string += str(card) + '\n'
        return deck_string

    def deal(self):
        random.shuffle(self.deck)
        dealer_hand = []
        player_hand = []
        for r in range(2):
            card = self.deck.pop()
            dealer_hand.append(str(card))
            self.sum1 += card.value

            card = self.deck.pop()
            player_hand.append(str(card))
            self.sum2 += card.value

        self.dealer.extend(dealer_hand)
        self.player.extend(player_hand)
        print(f'Player sum = {self.sum2}')

        return player_hand, dealer_hand

    def add_dealer_cards(self, cards):
        card = self.deck.pop()

        cards[1].append(str(card))
        self.player.extend(cards[1])
        self.sum1 = self.sum1 + int(card.value)
        return self.sum1

    def add_player_cards(self, cards):
        card = self.deck.pop()

        cards[0].append(str(card))
        self.dealer.extend(cards[0])
        self.sum2 = self.sum2 + int(card.value)
        return self.sum2


class Chips:

    def __init__(self, total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def show_balance(self):
        return self.total

    def win_bet(self):
        self.total = self.total + (self.bet * 2)
        self.bet = 0
        return self.total

    def lose_bet(self):
        self.bet = 0
        return self.total

    def take_bet(self):
        print(f'Your current balance is {self.total}')
        self.bet = int(input('How much do you want to bet?'))
        if self.bet <= self.total:
            self.total = self.total - self.bet
            cont = False
        else:
            print("Sorry! You don't have enough balance")
            print(f"Your balance is : {self.total}")
            print("Please enter yes to bet again")
            cont = True
        return cont


while playing:
    print("Welcome to BlackJack")
    show_card = Deck()
    show_cards = show_card.deal()

    def show_some():
        print(f'player has {show_cards[0]}')
        print(f'dealer has [\'{show_cards[1][0]}\']')

    def show_all():
        print(f'player has {show_cards[0]}')
        print(f'dealer has {show_cards[1]}')

    bet = Chips(total)
    show_some()
    choice = 1
    while choice == 1:
        while cont:
            cont = bet.take_bet()
        choice = int(input('Do you want a \'hit\' or \'stand\'?\nPress 1 for hit and press 2 for stand'))
        if choice == 1:
            add_card = show_card.add_player_cards(show_cards)
            show_all()
            print(f'Player\'s sum is {add_card}')
            if add_card == 21:
                print('\033[92mYou Won! Congratulations!!!\033[0m')
                total = bet.win_bet()
                Chips(total)
                v = bet.show_balance()
                print(f'The balance is {v}')
                bet.win_bet()
                break
            elif add_card > 21:
                print('\033[91mSorry! You are busted!!!\033[0m')
                total = bet.lose_bet()
                Chips(total)
                v = bet.show_balance()
                print(f'The balance is {v}')
                bet.lose_bet()
                if bet.lose_bet() == 0:
                    flag = 'sorry'
                    break
                break
            elif add_card < 21:
                continue
        elif choice == 2:
            add_dealer_card = show_card.add_dealer_cards(show_cards)
            show_all()
            print(f'Dearer\'s sum is {add_dealer_card}')
            if add_dealer_card == 21:
                print('\033[91mSorry! You lost! Dealer Won!!!\033[0m')
                total = bet.lose_bet()
                Chips(total)
                v = bet.show_balance()
                print(f'The balance is {v}')
                bet.lose_bet()
                if bet.lose_bet() == 0:
                    flag = 'sorry'
                    break
            elif add_dealer_card > 21:
                print('\033[92mCongratulations! You Won! Dealer Busted!!!\033[0m')
                total = bet.win_bet()
                Chips(total)
                v = bet.show_balance()
                print(f'The balance is {v}')
                bet.win_bet()
                break
            else:
                add_dealer_card = show_card.add_dealer_cards(show_cards)
                show_all()
                print(f'Dearer\'s sum is {add_dealer_card}')
                while add_dealer_card < 17:
                    add_dealer_card = show_card.add_dealer_cards(show_cards)
                    show_all()
                    print(f'Dearer\'s sum is {add_dealer_card}')

                if add_dealer_card == 21:
                    print('\033[91mSorry! You lost! Dealer Won!!!\033[0m')
                    total = bet.lose_bet()
                    Chips(total)
                    v = bet.show_balance()
                    print(f'The balance is {v}')
                    bet.lose_bet()
                    if bet.lose_bet() == 0:
                        flag = 'sorry'
                        break
                elif 17 <= add_dealer_card < 21:
                    print(add_dealer_card)
                    if add_dealer_card > add_card:
                        print('\033[91mSorry! You lost! Dealer Won!!!\033[0m')
                        total = bet.lose_bet()
                        Chips(total)
                        v = bet.show_balance()
                        print(f'The balance is {v}')
                        bet.lose_bet()
                        if bet.lose_bet() == 0:
                            flag = 'sorry'
                            break
                    elif add_dealer_card < add_card:
                        print('\033[92mCongratulations! You Won! Dealer Busted!!!\033[0m')
                        total = bet.win_bet()
                        Chips(total)
                        v = bet.show_balance()
                        print(f'The balance is {v}')
                        bet.win_bet()
                        break
                    else:
                        print('\033[94mIt is a draw\nPlay again\033[0m')
                        choice = 1
                elif add_dealer_card > 21:
                    print('\033[92mCongratulations! You Won! Dealer Busted!!!\033[0m')
                    total = bet.win_bet()
                    Chips(total)
                    v = bet.show_balance()
                    print(f'The balance is {v}')
                    bet.win_bet()
                    break
        else:
            print('You have entered wrong!Please enter again')
            choice = 1
    if flag == 'sorry':
        print('\033[95mYou are out of balance\nBetter luck next time\033[0m')
        cont = False
        playing = False
    else:
        det = input('Do you want to play again?\nPress \'ok\' to continue and press anything else to stop')
        if det == 'ok':
            playing = True
            cont = True
        else:
            print('\033[96mThanks for playing\nGame Over\033[0m')
            playing = False
