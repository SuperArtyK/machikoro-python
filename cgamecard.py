from card import *


#kludge for flags and macros
#instead of preprocessor
#card  types
GCARD_RESTAURANTS = 0 
GCARD_PRIMARY = 1
GCARD_SECONDARY = 2
GCARD_MAJOR = 3

#card type id
CARD_TYPE_GAMECARD = 1


#class for game cards, the ones that activate with dice roll
#card execution order: any turn; 
class GameCard(Card):
	#args: self, (str)name of card, (str)description of card, (int)execution type of card, (list of 2 int) execution dice roll
	def __init__(self, l_sname, l_sdesc, l_iGCType, l_idiceRoll, l_bHarborExpansion):
		super(GameCard, self).__init__(l_sname, l_sdesc, CARD_TYPE_GAMECARD, l_bHarborExpansion)
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
		return ("Card Title: %s\nDescription: %s\nActivates at: %s, when dice value is %d-%d" % (self.m_sName,self.m_sDesc,self.typeToStr(), self.m_iDiceRoll[0], self.m_iDiceRoll[1]))

class GCPrimary(GameCard):
	def __init__(self, l_sname, l_sdesc, l_idiceRoll, l_iIncome, l_bHarborExpansion):
		super(GCPrimary, self).__init__(l_sname, l_sdesc, GCARD_PRIMARY, l_idiceRoll, l_bHarborExpansion)
		self.m_iIncome = l_iIncome

	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player

	
	def cardaction(self, plr, card):
		
		print("DEBUG::call to GCPrimary::cardaction(plr)")
		for o in plr.m_lCards[GCARD_PRIMARY]:
			if(type(o) == type(card) ):
				plr.m_iCoins += o.m_iAmount * card.m_iIncome
				print("%s recieves %d coin(s) for %d %s(s)! (Total: %d)" % (plr.m_sName, o.m_iAmount * card.m_iIncome, o.m_iAmount, card.m_sName, plr.m_iCoins))
				return
		print("DEBUG::%s doesnt %s(s)!" % (plr.m_sName, card.m_sName))

