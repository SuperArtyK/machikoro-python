from card import *


#kludge for flags and macros
#instead of preprocessor
#card exec types
GCARD_EXEC_OTHER_TURN = 0
GCARD_EXEC_ANY_TURN = 1
GCARD_EXEC_YOUR_TURN = 2

#card type id
GCARD_TYPE_ID = 1

#class for game cards, the ones that activate with dice roll
#card execution order: any turn; 
class GameCard(Card):
	#args: self, (str)name of card, (str)description of card, (int)execution type of card, (list of 2 int) execution dice roll
	def __init__(self, l_sname, l_sdesc, l_iGCType, l_idiceRoll, l_iID):
		self = Card(l_sname, l_sdesc, GAME_CARD_TYPE_ID)
		self.m_iDiceRoll = l_idiceRoll
		self.m_iGCType = l_iGCType
		self.m_iID = l_iID
	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player
	def cardaction(self, plr):
		print("call to GameCard::cardaction(plr)")
	
	def typeToStr(self):
		if(self.m_iType == CARD_TYPE_ANY_TURN):
			return "Any turn"
		if(self.m_iType == CARD_TYPE_YOUR_TURN):
			return "Only your turn"
		if(self.m_iType == CARD_TYPE_OTHER_TURN):
			return "Only other player's turn"
	
	def __str__(self):
		return ("Card Title: %s\nDescription: %s\nActivates at: %s, when dice value is %d" % (self.m_sName,self.m_sDesc,self.typeToStr(), self.m_iDiceRoll))


GCARD_ID_NONE = 0 #dice: 0
GCARD_ID_SUSHI_BAR = 1 #1 other
GCARD_ID_WHEAT_FIELD = 2 #1 any
GCARD_ID_FARM = 3 #2 any
GCARD_ID_BAKERY = 4 #2-3 your
GCARD_ID_CAFE = 5 #3 other
GCARD_ID_FLOWER_GARDEN = 6 #4 any
GCARD_ID_SHOP = 7 #4 your
GCARD_ID_FOREST = 8 #5 any


