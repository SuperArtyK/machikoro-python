#i guess bad pracice
from card import *
from cgamecard import *

class CWheatField(GCPrimary):

	def __init__(self):
		#Card.__init__(self, "Wheat Field", "Receive 1 coin from the bank. At any turn", CARD_TYPE_ANY_TURN, 1)
		super(CWheatField, self).__init__("Wheat Field", "Recieve 1 coin from the bank", [1,1])
		
	def cardaction(self, plr):
		plr.m_iCoins +=1
