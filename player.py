#i guess bad pracice
from card import *
from cwheat import *


#class of player that posesses the cards themselves
class Player:
	def __init__(self, l_sname):
		self.m_sName = l_sname
		#list of card obj+int, game cards and amount that player owns
		#ex [wheatfield, 1] -- 1 wheatfield card
		self.m_lCards = []
		self.m_iCoins = 3
		#list of card obj+bool, attractions that player have built
		self.m_lAttractions = []
	#add card to the list
	#args: self, Card object
	def addcard(self, card):
		print("Entered addcard")
		print("Card is "+card.m_sName)
		if(card.m_iID > 0):
			print("Card is a game card")
			for o in self.m_lCards:
				pass
		elif (card.m_iID < 0):
			print("Card is an attraction card")
			for i in range(len(self.m_lAttractions)//2):
				if(type(card) == type(self.m_lAttractions[i*2])):
					if(self.m_lAttractions[i+1] == True):
						print("You cannot build more than 1 of each attraction card!")
						return
					self.m_lAttractions[i+1] = True
					print("Added card "+card.m_sName)
					return
