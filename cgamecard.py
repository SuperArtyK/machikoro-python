from card import *
from eventprint import *


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
	def __init__(self, l_sname, l_sdesc, l_iGCType, l_idiceRoll, l_bHarborExpansion, l_iMaxAmount, l_iPrice):
		super(GameCard, self).__init__(l_sname, l_sdesc, CARD_TYPE_GAMECARD, l_bHarborExpansion, l_iMaxAmount, l_iPrice)
		printd("Creating GameCard() ->  %s" % (l_sname))
		self.m_iDiceRoll = l_idiceRoll
		self.m_iGCType = l_iGCType
	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player
	def cardaction(self, plr):
		printd("call to GameCard::cardaction(plr)")
	
	def typeToStr(self):
		if(self.m_iType == GCARD_PRIMARY):
			return "Any turn"
		if(self.m_iType == GCARD_SECONDARY):
			return "Only your turn"
		if(self.m_iType == GCARD_RESTAURANTS):
			return "Only other player's turn"
	
	def __str__(self):
		return ("Game Card Title: %s\nDescription: %s\nActivates at: %s, when dice value is %d-%d\nCosts: %d coins\nFrom Harbor Expansion: %r" % (self.m_sName,self.m_sDesc,self.typeToStr(), self.m_iDiceRoll[0], self.m_iDiceRoll[1], self.m_iPrice, self.m_bHarborExpansion))




class GCPrimary(GameCard):
	def __init__(self, l_sname, l_sdesc, l_idiceRoll, l_iIncome, l_bHarborExpansion, l_iPrice):
		super(GCPrimary, self).__init__(l_sname, l_sdesc, GCARD_PRIMARY, l_idiceRoll, l_bHarborExpansion, 6, l_iPrice)
		printd("Creating GCPrimary() ->  %s" % (l_sname))
		self.m_iIncome = l_iIncome

	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player

	
	def cardaction(self, plr, card):
		
		printd("call to GCPrimary::cardaction()")
		for o in plr.m_lCards[GCARD_PRIMARY]:
			if(type(o) == type(card) ):
				plr.m_iCoins += o.m_iAmount * card.m_iIncome
				printe("Player %s recieves %d coin(s) for %d %s(s)! (Total: %d)" % (plr.m_sName, o.m_iAmount * card.m_iIncome, o.m_iAmount, card.m_sName, plr.m_iCoins), MEVENT_ADD_COINS)
				return
		printd("%s doesnt have %s(s)! Why did you even called this function, if it's not going to do anything, you stu..." % (plr.m_sName, card.m_sName))

class GCSecondary(GameCard):
	def __init__(self, l_sname, l_sdesc, l_idiceRoll, l_iIncome, l_bHarborExpansion, l_bShopAffected, l_iPrice):
		super(GCSecondary, self).__init__(l_sname, l_sdesc, GCARD_PRIMARY, l_idiceRoll, l_bHarborExpansion, 6, l_iPrice)
		printd("Creating GCSecondary() ->  %s" % (l_sname))
		self.m_iIncome = l_iIncome
		#if shopping mall landmark affects the card
		self.m_bShopAffected = l_bShopAffected

	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player

	
	def cardaction(self, plr, card):		
		printd("call to GCSecondary::cardaction()")
		for o in plr.m_lCards[GCARD_PRIMARY]:
			if(type(o) == type(card)):
				if(plr.m_lLandmanrs[3] and card.m_bShopAffected):
					plr.m_iCoins += o.m_iAmount * (card.m_iIncome+1)
					printe("%s recieves %d coin(s) for %d %s(s) with Shopping Mall! (Total: %d)" % (plr.m_sName, o.m_iAmount * (card.m_iIncome+1), o.m_iAmount, card.m_sName, plr.m_iCoins), MEVENT_ADD_COINS)
				else:
					plr.m_iCoins += o.m_iAmount * card.m_iIncome
					printe("Player %s recieves %d coin(s) for %d %s(s)! (Total: %d)" % (plr.m_sName, o.m_iAmount * card.m_iIncome, o.m_iAmount, card.m_sName, plr.m_iCoins), MEVENT_ADD_COINS)
				return
		printd("%s doesnt have %s(s)! Why did you even called this function, if it's not going to do anything, you stu..." % (plr.m_sName, card.m_sName))