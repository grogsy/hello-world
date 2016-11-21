class Card:
	'represents a playing card'
	def __init__(self, rank, suit):
		'initialize rank and suit of playing card'
		self._rank = rank
		self._suit = suit
	
	@property
	def rank(self):
		'return rank'
		return self._rank
	@property
	def suit(self):
		'return suit'
		return self._suit
	def __repr__(self):
		'display (rank, suit)'
		return "Card('{}', '{}')".format(self.rank, self.suit)
	def __eq__(self, other):
		'return True if self and other have same (rank, suit)'
		return self.rank == other.rank and self.suit == other.suit
	def __lt__(self, other):
		'return True if self.rank < other.rank'
		return self.rank < other.rank
	def __gt__(self, other):
		'return True if self.rank > other.rank'
		return self.rank > other.rank
	def __str__(self):
		'returns a prettified print version of suit and rank'
		return "{} {}".format(self.rank, self.suit)
	value = property(__str__)
from random import shuffle
class Deck:
	'represents a deck of 52 cards'
		
	#ranks and suits are Deck class variables
	_ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
		
	#suits is a set of 4 Unicode symbols representing the 4 suits
	_suits = {'Hearts','Spades','Clovers','Diamonds'}
		
	def __init__(self):
		'initialize deck of 52 cards'
		self._cards = []			# deck is initially empty
			
		for suit in Deck._suits:
			for rank in Deck._ranks:
				#add Card with given rank and suit to deck
				self._cards.append(Card(rank, suit))
	@property
	def cards(self):
		return self._cards
	def dealCard(self):
		'deal (pop and return) card from the top of the deck'
		return self.cards.pop()
		
	def shuffle(self):
		'shuffle the deck'
		shuffle(self.cards)
	def __len__(self):
		'return the length of deck'
		return len(self.cards)
	def __eq__(self, other):
		'return True if two decks contain the same cards in the same order'
		return self.cards == other.cards
	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

class Hand(Deck):
	'Represents a hand of playing cards'
	def __init__(self, label=''):
		self._cards = []
		self._label = label
	@property
	def label(self):
		return self._label
		
	def addCard(self, card):
		'add card to players hand'
		return self.cards.append(card)
	def total(self):
		'returns the value of the hand'
		values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
				  '9':9, '10': 10, 'J':10, 'Q':10, 'K':10, 'A':11}
		res    = 0
		aces   = 0
		for card in self.cards:
			res += values[card.rank]
			if card.rank == 'A':
				aces += 1
		while res > 21 and aces > 0:
			res  -=10
			aces -=1
		return res
		
	def __str__(self):
		return "Hand:{}\nCards:\n{}".format(self.label, Deck.__str__(self))

def compareHands(house, player):
	'compares house and player hands and prints outcome'
	
	if house.total()   > player.total(): print('You lose.')
	elif house.total() < player.total(): print('You win!')
	elif house.total()  == 21 and 2 == len(house)  < len(player): print('You lose.')
	elif player.total() == 21 and 2 == len(player) < len(house): print('You win!')
	else:
		print('A tie.')

def dealCard(deck, participant):
	'deals a single card from deck to participant'
	card = deck.dealCard()
	participant.addCard(card)
	return card
		
def game():
	'simulates a game of blackjack'
	
	deck   = Deck()
	deck.shuffle()
	house  = Hand('House')
	player = Hand('Player')
	
	for i in range(2):
		dealCard(deck, player)				#deal cards
		dealCard(deck, house)				#to participants
		
	print(house)							#print
	print(player)							#state of the table
	
	answer = input('Hit or stand? (default: hit)')
	while answer in {'', 'h', 'hit'}:
		card = dealCard(deck, player)
		print("You got: {}".format(card))
		if player.total() > 21:
			print('You went over, you lose')
			return
	
		answer = input('Hit or stand? (default: hit)')
	while house.total() < 17:
		card = dealCard(deck, house)
		print("House got: {}".format(card))
		if house.total() > 21:
			print('House went over, You win!')
			return
	compareHands(house, player)
	
if __name__ == '__main__':
	game()
	
	