from card import *


#kludge for flags and macros
#instead of preprocessor
#card  types
GCARD_RESTAURANTS = 0 
GCARD_PRIMARY = 1
GCARD_SECONDARY = 2

#card type id
GCARD_TYPE_ID = 1

#class for game cards, the ones that activate with dice roll
#card execution order: any turn; 
class GameCard(Card):
	#args: self, (str)name of card, (str)description of card, (int)execution type of card, (list of 2 int) execution dice roll
	def __init__(self, l_sname, l_sdesc, l_iGCType, l_idiceRoll):
		super(GameCard, self).__init__(l_sname, l_sdesc, GCARD_TYPE_ID)
		self.m_iDiceRoll = l_idiceRoll
		self.m_iGCType = l_iGCType
	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player
	def cardaction(self, plr):
		print("call to GameCard::cardaction(plr)")
	
	def typeToStr(self):
		if(self.m_iType == GCARD_PRIMARY):
			return "Any turn"
		if(self.m_iType == GCARD_SECONDARY):
			return "Only your turn"
		if(self.m_iType == GCARD_RESTAURANTS):
			return "Only other player's turn"
	
	def __str__(self):
		return ("Card Title: %s\nDescription: %s\nActivates at: %s, when dice value is %s" % (self.m_sName,self.m_sDesc,self.typeToStr(), "-".join(self.m_iDiceRoll)))

class GCPrimary(GameCard):
	def __init__(self, l_sname, l_sdesc, l_idiceRoll):
		super(GCPrimary, self).__init__(l_sname, l_sdesc, GCARD_PRIMARY, l_idiceRoll)

	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player
	def cardaction(self, plr):
		print("call to GCPrimary::cardaction(plr)")

