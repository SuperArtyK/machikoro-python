#list of all gamecards

#i guess bad pracice
from card import *
from cgamecard import *


#primary card
GAMECARD_ID_WHEATFIELD = 1

#wheat field
#1 coin at any turn
#6 supply, 5 in starter deck
#max player can have: 7
class CWheatField(GCPrimary):

	def __init__(self):
		#Card.__init__(self, "Wheat Field", "Receive 1 coin from the bank. At any turn", CARD_TYPE_ANY_TURN, 1)
		super(CWheatField, self).__init__("Wheat Field", "Recieve 1 coin from the bank",
			[1,1], 1, False, 1, "+1 coin", GAMECARD_ID_WHEATFIELD, 'Crops')

		
	def cardAction(self, plr):
		super().cardAction(plr, self)


GAMECARD_ID_RANCH = 2
#ranch
#1 coin at any turn
#6 supply
class CRanch(GCPrimary):

	def __init__(self):
		super(CRanch, self).__init__("Ranch", "Recieve 1 coin from the bank",
			[1,1], 1, False, 1, "+1 coin", GAMECARD_ID_RANCH, 'Livestock')

		
	def cardAction(self, plr):
		super().cardAction(plr, self)


GAMECARD_ID_FLOWERORCHARD = 4
#Flower Orchard
#1 coin at any turn
#6 supply
class CFlowerOrchard(GCPrimary):

	def __init__(self):
		super(CFlowerOrchard, self).__init__("Flower Orchard", "Recieve 1 coin from the bank",
			[1,1], 1, False, 2, "+1 coin", GAMECARD_ID_FLOWERORCHARD, 'Crops')

		
	def cardAction(self, plr):
		super().cardAction(plr, self)

