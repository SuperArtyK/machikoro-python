from card import *
from eventprint import *


#kludge for flags and macros
#instead of preprocessor
#card  types
GAMECARD_ID_RESTAURANTS = 0 
GAMECARD_ID_PRIMARY = 1
GAMECARD_ID_SECONDARY = 2
GAMECARD_ID_MAJOR = 3
GAMECARD_NAMES = ["Restaurant", "Primary Establishment", "Secondary Establishment", "Major Establishment", ]

#card type id
CARD_TYPE_GAMECARD = 1


#class for game cards, the ones that activate with dice roll
#card execution order: any turn; 
class GameCard(Card):
	#args: self, (str)name of card, (str)description of card, (int)execution type of card, (list of 2 int) execution dice roll, 
	#is from harbor expansion?, price, shortened desrciption, card ID, card category
	def __init__(self, l_sname, l_sdesc, l_iGCType, l_lDiceRoll, l_bHarborExpansion, l_iPrice, l_sShortDesc, l_iID, l_sCategory):
		super(GameCard, self).__init__(l_sname, l_sdesc, CARD_TYPE_GAMECARD, l_bHarborExpansion, l_iPrice, l_sShortDesc, l_iID)
		printd("Creating GameCard() ->  %s" % (l_sname))
		self.m_lDiceRoll = l_lDiceRoll
		self.m_iGCType = l_iGCType
		self.m_sCategory = l_sCategory
		
	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player
	def cardAction(self, plr):
		printd("call to GameCard::cardaction(plr)")
	
	def execTypeToStr(self):
		if(self.m_iType == GAMECARD_ID_PRIMARY):
			return "Any turn"
		if(self.m_iType == GAMECARD_ID_SECONDARY or self.m_iType == GAMECARD_ID_MAJOR):
			return "Only your turn"
		if(self.m_iType == GAMECARD_ID_RESTAURANTS):
			return "Only other player's turn"
			
	def typeToStr(self):
		if(self.m_iType == GAMECARD_ID_RESTAURANTS):
			return "Restaurants"
		elif(self.m_iType == GAMECARD_ID_PRIMARY):
			return "Primary"
		elif(self.m_iType == GAMECARD_ID_SECONDARY):
			return "Secondary"
		elif(self.m_iType == GAMECARD_ID_MAJOR):
			return "Major"
	
	def __str__(self):
		return ("Game Card Title: %s\nDescription: %s\nType: %s\nCategory: %s\nActivates at: %s, when dice value is %d-%d\nCosts: %d coins\nFrom Harbor Expansion: %r" % (self.m_sName,self.m_sDesc,self.typeToStr(), self.m_sCategory, self.execTypeToStr(), self.m_lDiceRoll[0], self.m_lDiceRoll[1], self.m_iPrice, self.m_bHarborExpansion))




class GCPrimary(GameCard):
	def __init__(self, l_sname, l_sdesc, l_idiceRoll, l_iIncome, l_bHarborExpansion, l_iPrice, l_sShortDesc, l_iID, l_sCategory):
		super(GCPrimary, self).__init__(l_sname, l_sdesc, GAMECARD_ID_PRIMARY, l_idiceRoll, l_bHarborExpansion, l_iPrice, l_sShortDesc, l_iID, l_sCategory)
		printd("Creating GCPrimary() ->  %s" % (l_sname))
		self.m_iIncome = l_iIncome

	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player

	
	def cardAction(self, plr, card):
		
		printd("call to GCPrimary::cardaction()")
		for o in plr.m_lGamecards[GAMECARD_ID_PRIMARY]:
			if(type(o) == type(card) ):
				plr.m_iCoins += o.m_iAmount * card.m_iIncome
				printe("Player %s recieves %d coin(s) for %d %s(s)! (Total: %d)" % (plr.m_sName, o.m_iAmount * card.m_iIncome, o.m_iAmount, card.m_sName, plr.m_iCoins), MEVENT_ADD_COINS)
				return
		printd("%s doesnt have %s(s)! Why did you even called this function, if it's not going to do anything, you stu..." % (plr.m_sName, card.m_sName))

class GCSecondary(GameCard):
	def __init__(self, l_sname, l_sdesc, l_idiceRoll, l_iIncome, l_bHarborExpansion, l_bShopAffected, l_iPrice, l_sShortDesc, l_iID, l_sCategory):
		super(GCSecondary, self).__init__(l_sname, l_sdesc, GAMECARD_ID_PRIMARY, l_idiceRoll, l_bHarborExpansion, l_iPrice, l_sShortDesc, l_iID, l_sCategory)
		printd("Creating GCSecondary() ->  %s" % (l_sname))
		self.m_iIncome = l_iIncome
		#if shopping mall landmark affects the card
		self.m_bShopAffected = l_bShopAffected

	#declare a cardaction fn in each class inherited
	#args are: self and obj of Player

	
	def cardAction(self, plr, card):		
		printd("call to GCSecondary::cardaction()")
		for o in plr.m_lGamecards[GAMECARD_ID_PRIMARY]:
			if(type(o) == type(card)):
				if(plr.m_lLandmanrs[3] and card.m_bShopAffected):
					plr.m_iCoins += o.m_iAmount * (card.m_iIncome+1)
					printe("%s recieves %d coin(s) for %d %s(s) with Shopping Mall! (Total: %d)" % (plr.m_sName, o.m_iAmount * (card.m_iIncome+1), o.m_iAmount, card.m_sName, plr.m_iCoins), MEVENT_ADD_COINS)
				else:
					plr.m_iCoins += o.m_iAmount * card.m_iIncome
					printe("Player %s recieves %d coin(s) for %d %s(s)! (Total: %d)" % (plr.m_sName, o.m_iAmount * card.m_iIncome, o.m_iAmount, card.m_sName, plr.m_iCoins), MEVENT_ADD_COINS)
				return
		printd("%s doesnt have %s(s)! Why did you even called this function, if it's not going to do anything, you stu..." % (plr.m_sName, card.m_sName))