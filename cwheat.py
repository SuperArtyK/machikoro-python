#i guess bad pracice
from card import *
from cgamecard import *

class CWheatField(GameCard):

	def __init__(self):
		#Card.__init__(self, "Wheat Field", "Receive 1 coin from the bank. At any turn", CARD_TYPE_ANY_TURN, 1)
		GameCard("Wheat Field", "Recieve 1 coin from the bank", GCARD_TYPE_ANY_TURN, [1,1] 1)
		self.m_iID = 1
		return
	def cardaction(self, plr):
		plr.m_iCoins +=1
