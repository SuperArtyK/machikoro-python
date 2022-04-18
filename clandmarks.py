from decimal import Clamped
from card import *

CARD_TYPE_LANDMARK = 2

class CLandmark(Card):
	def __init__(self, l_sname, l_sdesc, l_bHarborExpansion, l_iPrice):
		super().__init__(l_sname, l_sdesc, CARD_TYPE_LANDMARK, l_bHarborExpansion, 5, l_iPrice)
		printd("Creating CLandmark() ->  %s" % (l_sname))

	def __str__(self):
		return ("Landmark Title: %s\nDescription: %s" % (self.m_sName, self.m_sDesc))

class CCityHall(CLandmark):
	def __init__(self):
		super().__init__("City Hall", "Immediately before buying establishments, if you have 0 coins, get 1 from the bank.", CARD_TYPE_LANDMARK, True, 5, 0) #costs nothing built immediately

class CCityHall(CLandmark):
	def __init__(self):
		super().__init__("City Hall", "Immediately before buying establishments, if you have 0 coins, get 1 from the bank.", CARD_TYPE_LANDMARK, True, 5, 0) #costs nothing built immediately

