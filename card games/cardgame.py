import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_suit(self):
        if self.suit == 0:
            return 'S'
        elif self.suit == 1:
            return 'C'
        elif self.suit == 2:
            return 'D'
        elif self.suit == 3:
            return 'H'
    
    def get_rank(self):
        if self.rank > 1 and self.rank < 11:
            return str(self.rank)
        elif self.rank == 11:
            return 'J'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 13:
            return 'K'
        elif self.rank == 1:
            return 'A'
        else:
            return 'you have some invalid rank'
        
    def __repr__(self):
        suit = self.get_suit()
        rank = self.get_rank()
        return '{}{}'.format(rank, suit)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(1,14):
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

class Player:
    def __init__(self):
        self.hand = []    

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player()
        self.player = Player()
    
    def deal_cards(self):
        for i in range(2):
            card1 = self.deck.deck.pop()
            card2 = self.deck.deck.pop()
            self.player.hand.append(card1)
            self.dealer.hand.append(card2)
        pass

    def reset(self):
        self.player.hand = []
        self.dealer.hand = []
        pass

    def hit(self, player):
        card = self.deck.deck.pop()
        player.hand.append(card)

    def get_hand_value(self, player):
        hand = player.hand
        value1 = 0
        value2 = 0
        for card in player.hand:
            if card.rank > 10:
                value1 += 10
                value2 += 10
            elif card.rank == 1:
                value1 += 1
                value2 += 11
            else:
                value1 += card.rank
                value2 += card.rank
        if value1 == value2:
            return value1
        elif value2 <= 21:
            return value2
        else:
            return value1
         

    def play(self):
        play = 'y'
        while play == 'y':
            self.deck.shuffle()
            self.deal_cards()
            print('Dealer shows {}'.format(self.dealer.hand[0]))
            print(self.player.hand)
            print(self.get_hand_value(self.player))
            # ask player to make a move until stand or bust
            move = ''
            while move != '2':
                move = input('[1] hit, [2] stand: ')
                if move == '1':
                    self.hit(self.player)
                    print(self.player.hand)
                    print(self.get_hand_value(self.player))
            
            # Then dealer plays until stand or bust


            # compute score
            if self.get_hand_value(self.player) > 21 and self.get_hand_value(self.dealer) > 21:
                print('Both of you bust!')
            elif self.get_hand_value(self.player) > 21:
                print('You bust!')
            elif self.get_hand_value(self.dealer) > 21:
                print('Dealer busts!')
            elif self.get_hand_value(self.dealer) > self.get_hand_value(self.player):
                print('Dealer wins!')
            elif self.get_hand_value(self.dealer) < self.get_hand_value(self.player):
                print('You win!')
            else:
                print('It\'s a tie!')
            # ask player to play again
            self.reset()
            play = input('Play again? y/n: ')

        print('See you next time!')
        

game = Blackjack()
game.play()