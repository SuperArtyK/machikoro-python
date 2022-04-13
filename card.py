#card ids
#game card = 1
#attractions = 2
#just card = 0

CARD_TYPE_ID = 0

#card class
#base class of all game cards
class Card:
	#self, card name, card description, card execution type, execution dice roll, is card from advanced set
	def __init__(self, l_sname, l_sdesc, l_itype):
		self.m_sName = l_sname
		self.m_sDesc = l_sdesc
		self.m_iType = l_itype
		
	def __str__(self):
		return ("Card Title: %s\nDescription: %s" % (self.m_sName, self.m_sDesc))

