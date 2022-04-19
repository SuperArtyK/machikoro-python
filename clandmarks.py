from decimal import Clamped
from card import *

CARD_TYPE_LANDMARK = 2

class CLandmark(Card):
	def __init__(self, l_sname, l_sdesc, l_bHarborExpansion, l_iPrice):
		#idk how to use max limit of 5 cards, player discards 2nd same landmark anyway.
		super().__init__(l_sname, l_sdesc, CARD_TYPE_LANDMARK, l_bHarborExpansion, 5, l_iPrice)
		printd("Creating CLandmark() ->  %s" % (l_sname))

	def __str__(self):
		return (">Landmark Title: %s\n>Description: %s\n>Costs: %d coins\n>From Harbor Expansion: %r" % (self.m_sName, self.m_sDesc, self.m_iPrice, self.m_bHarborExpansion))

class CCityHall(CLandmark):
	def __init__(self):
		super().__init__("City Hall", "Immediately before buying establishments, if you have 0 coins, get 1 from the bank.", True, 0) #costs nothing built immediately

class CHarbor(CLandmark):
	def __init__(self):
		super().__init__("Harbor", "If the dice total is 10 or more, you may add 2 to the total, on your turn only.", True, 2)

class CTrainStation(CLandmark):
	def __init__(self):
		super().__init__("Train Station", "You may roll 1 or 2 dice.", False, 4)

#TODO: Add proper description to this card.
class CShoppingMall(CLandmark):
	def __init__(self):
		super().__init__("Shopping Mall", "Recieve 1 more coin for your restaurants and secondary ", False, 10)

class CAmusementPark(CLandmark):
	def __init__(self):
		super().__init__("Amusement Park", "If you roll doubles, take another turn after this one.", False, 16)

class CRadioTower(CLandmark):
	def __init__(self):
		super().__init__("Radio Tower", "Once every turn, you can choose to re-roll your die/dice.", False, 22)

class CAirport(CLandmark):
	def __init__(self):
		super().__init__("Airport", "If you build nothing on your turn, you get 10 coins from the bank.", True, 30)
