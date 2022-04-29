from decimal import Clamped
from card import *

CARD_TYPE_LANDMARK = 2

LANDMARK_ID_NONE= -1
LANDMARK_ID_CITYHALL = 0
LANDMARK_ID_HARBOR = 1
LANDMARK_ID_TRAINSTATION = 2
LANDMARK_ID_SHOPPINGMALL = 3
LANDMARK_ID_AMUSEMENTPARK = 4
LANDMARK_ID_RADIOTOWER = 5
LANDMARK_ID_AIRPORT = 6

#base landmark class
class CLandmark(Card):
	def __init__(self, l_sname, l_sdesc, l_bHarborExpansion, l_iPrice, l_sShortDesc, l_iID):
		#idk how to use max limit of 5 cards, player discards 2nd same landmark anyway.
		super().__init__(l_sname, l_sdesc, CARD_TYPE_LANDMARK, l_bHarborExpansion, 5, l_iPrice, l_sShortDesc, l_iID)
		printd("Creating CLandmark() ->  %s" % (l_sname))

	def __str__(self):
		return ("Landmark Title: %s\nDescription: %s\nCosts: %d coins\nFrom Harbor Expansion: %r" % (self.m_sName, self.m_sDesc, self.m_iPrice, self.m_bHarborExpansion))



#landmarks

class CCityHall(CLandmark):
	def __init__(self):
		super().__init__("City Hall", "Immediately before buying establishments, if you have 0 coins, get 1 from the bank.", 
			True, 0, "Before buying, you always have 1 coin", LANDMARK_ID_CITYHALL) #costs nothing built immediately

class CHarbor(CLandmark):
	def __init__(self):
		super().__init__("Harbor", "If the dice total is 10 or more, you may add 2 to the total, on your turn only.",
			True, 2, "If dice val is 10+, you may make it 12(your turn) ", LANDMARK_ID_HARBOR)

class CTrainStation(CLandmark):
	def __init__(self):
		super().__init__("Train Station", "You may roll 1 or 2 dice.", 
			False, 4, "You may roll 2 dice", LANDMARK_ID_TRAINSTATION)

#TODO: Add proper description to this card.
class CShoppingMall(CLandmark):
	def __init__(self):
		super().__init__("Shopping Mall", "Recieve 1 more coin for your restaurants and <secondary>)",
			False, 10, "+1c for restaurants and <secondary> pay", LANDMARK_ID_SHOPPINGMALL)

class CAmusementPark(CLandmark):
	def __init__(self):
		super().__init__("Amusement Park", "If you roll doubles, take another turn after this one.",
			False, 16, "take another turn if you roll doubles", LANDMARK_ID_AMUSEMENTPARK)

class CRadioTower(CLandmark):
	def __init__(self):
		super().__init__("Radio Tower", "Once every turn, you can choose to re-roll your die/dice.",
			False, 22, "you may re-roll your die/dice once", LANDMARK_ID_RADIOTOWER)

class CAirport(CLandmark):
	def __init__(self):
		super().__init__("Airport", "If you build nothing on your turn, you get 10 coins from the bank.",
			True, 30, "+10c if you don't build in this turn", LANDMARK_ID_AIRPORT)
