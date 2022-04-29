#list of all gamecards

#i guess bad pracice
from card import *
from cgamecard import *

#ids
GAMECARD_ID_WHEATFIELD = 1

#wheat field
#1 coin at any turn
#6 supply, 5 in starter deck
#max player can have: 7
class CWheatField(GCPrimary):

	def __init__(self):
		#Card.__init__(self, "Wheat Field", "Receive 1 coin from the bank. At any turn", CARD_TYPE_ANY_TURN, 1)
		super(CWheatField, self).__init__("Wheat Field", "Recieve 1 coin from the bank",
			[1,1], 1, False, 6, "+1 coin", GAMECARD_ID_WHEATFIELD)

		
	def cardAction(self, plr):
		super().cardAction(plr, self)

