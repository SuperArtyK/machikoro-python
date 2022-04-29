#contains class of player that posesses the cards themselves

#i guess bad pracice
from card import *
from cgclist import *
from clandmarks import *
from eventprint import *

#internal use only: player count
_PLAYER_COUNT = 0
#internal use only: deck of all cards in the game
_GAMECARD_DECK = [CWheatField()]
_LANDMARK_DECK = [CCityHall(), CHarbor(), CTrainStation(), CShoppingMall(), CAmusementPark(), CRadioTower(), CAirport()]

def getLandmarkDeck():
	return _LANDMARK_DECK

def getGamecardDeck():
	return _GAMECARD_DECK

def isCardInList(itm, lst):
	#check if list a multidimensional list
	#or whatever, list with lists
	if(len(lst)):
		if(isinstance(lst[0], list)):
			for o in lst:
				if(isCardInList(itm, o)):
					return True
		else:
			for o in lst:
				if o.m_iType == itm.m_iType and o.m_iID == itm.m_iID:
						return True
	return False


#class itself
class Player:
    #constructor
	def __init__(self, l_sName):
		self.m_sName = l_sName
		global _PLAYER_COUNT
		_PLAYER_COUNT +=1
		printe("Player %s has entered the game! (Total: %d players)" % (self.m_sName, _PLAYER_COUNT), MEVENT_ADD_PLAYER)
		#list lists, each sublist indicates GameCard type, such as GCARD_PRIMARY, ~SECONDARY, etc
		#order is same as gamecard Type id
		#each sublist contains already built cards
		self.m_lGamecards = [ [], [], [], [] ]
		self.m_iCoins = 3
		#list of landmark objs, landmarks that player have built, as follows(price ascending):
		#City Hall, Harbor, Train Station, Shopping Mall, Amusement Park, Radio Tower, Airport
		#City hall is always built, from start
		self.m_lLandmarks = []
		#TODO:Add bakery here!
		printd("Adding default cards to player: City Hall 1x; Wheat Field 1x")
		self.addCard(CCityHall(), True)
		self.addCard(CWheatField(), True)
		
		
	#add card to the list
	#args: self, Card object
	#TODO: Put "adding card" to "buycard"
	def addCard(self, card:Card, bDontCreate = False):
		printe("Adding card %s to player %s" % (card.m_sName, self.m_sName), MEVENT_ADD_CARD)
		printd("Entered addcard")
		printd("Card is: "+card.m_sName)
		if(card.m_iType == CARD_TYPE_LANDMARK):
			printd("Instance of landmark")
			#TODO: change from 'type() ==' to landmark.id check in m_lLandmarks
			if(isCardInList(card, self.m_lLandmarks)):
				printe("You cannot build more than 1 same landmark!", MEVENT_ERROR)
				return
			
			if(bDontCreate):
				self.m_lLandmarks.append(card)
			else:
				self.m_lLandmarks.append(card.__class__())
		elif(card.m_iType == CARD_TYPE_GAMECARD):
			printd("Instance of gamecard: " + card.typeToStr())
			#check if card is major, same outcome as landmarks
			for o in self.m_lGamecards[card.m_iGCType]:
				if(type(o) is type(card)): #match!
					printd("Found same card in card list")
					if(card.m_iGCType == GAMECARD_ID_MAJOR):#what if major?
						printe("You cannot build more than 1 same Major Establishment!", MEVENT_ERROR)
					else:
						o.m_iAmount +=1 #increase amount
						printd("Incrementing card amount: %d" % (o.m_iAmount))
					return #return anyway. deed is done
			#oi, looks like we didnt have any cards in list
			#add it quickly!
			printd("Card didn't exist in the list; adding...")
			if(bDontCreate):
				self.m_lGamecards[card.m_iGCType].append(card)
			else:
				self.m_lGamecards[card.m_iGCType].append(card.__class__())


	#lists cards of a player with optional filter applied
	#args: type of cards to display:
	#0 -- all, 10 -- all landmarks, 11 -- unbuilt landmarks, 12 -- built landmarks, 
	# 20 -- all built gamecards(+status built/unbuilt), 21 -- unbuilt gamecards, 22 -- built gamecards
	# 30/31/32 -- restaurants, 40/41/42 -- primary, 50/51/52 -- secondary, 60/61/62 -- major
	def listCards(self, iType:str = '00'):
		iType = str(iType)
		listDeck(self, iType)
		pass
	
	def hasCard(self, card:Card):
		result = 0
		result += isCardInList(card, self.m_lGamecards)
		result += isCardInList(card, self.m_lLandmarks)
		#playing with bool conversion. 0 is false and anything else is True
		return result
	

#do not call, internal usage only!
#args: filter type, list to output, list to use as Filter data(optional)
#iFilterType: 
#0 -- just print the cards if 2nd list given, mark if does(n't) exist
#1 -- cards NOT in the 2nd list
#2 -- cards IN the 2nd list
def _listDeck(iFilterType:str, lst, lst2 = None):
	if(len(lst) == 0):
		printe(" 0: None", MEVENT_CARD)
		return False 
	tmp = []
	if(iFilterType[0] == '1'): #only unbuilt cards
		for i in lst:#slow af
			if(not isCardInList(i, lst2)):
				printd('Card %s is not in the list' % (i.m_sName))
				tmp.append(i)
		printd("List: ")
		for i in tmp:#slow af
			printd(i.m_sName)
		_listDeck('0', tmp)
	elif(iFilterType[0] == '2'): #only built cards
		for i in lst:#slow af
			for j in lst2:
				if(type(i) is type(j)):
					tmp.append(i)
		_listDeck('0', tmp)
	#TODO: Remove iteration by index
	#TODO: Add ID to gamecards
	elif(iFilterType[0] == '0'):
		for i in range(len(lst)):
			if(lst[i].m_iType == CARD_TYPE_GAMECARD):
				printe("%2d:%s %s;%sActivation:%2d-%d,%sCost:%2d, Type:%s, Description: %s" % 
					(i+1, 
					('' if (lst2 is None) else " (built)  " if (isCardInList(lst[i], lst2)) else " (unbuilt)"),
					lst[i].m_sName, ' '*(27-len(lst[i].m_sName)), lst[i].m_lDiceRoll[0], lst[i].m_lDiceRoll[1],
					#now THIS is a kludge. convert number to a string and then calculate it's length
					" "*len(str(lst[i].m_lDiceRoll[1])), 
					lst[i].m_iPrice, lst[i].typeToStr(), lst[i].m_sShortDesc), MEVENT_GAMECARD)
			elif(lst[i].m_iType == CARD_TYPE_LANDMARK):
				printe("%2d:%s %s;%sCost:%2d, Description: %s" % 
					(lst[i].m_iID+1, 
					('' if (lst2 is None) else " (built)  " if (isCardInList(lst[i], lst2)) else " (unbuilt)"),
					lst[i].m_sName, ' '*(16-len(lst[i].m_sName)), lst[i].m_iPrice, lst[i].m_sShortDesc), MEVENT_LANDMARK)
		
	else:
		return False #fail, type didn't match
	return True #success!

#args: optional Player type, 
#list deck with possible filters to player
# 00 -- all, 01 -- all unbuilt cards, 02 -- all built cards
# 10 -- all landmarks, 11 -- unbuilt landmarks, 12 -- built landmarks, 
# 20 -- all built gamecards(+status built/unbuilt), 21 -- unbuilt gamecards, 22 -- built gamecards
# 30/31/32 -- restaurants, 40/41/42 -- primary, 50/51/52 -- secondary, 60/61/62 -- major
#TODO: print error if iType is wrong
#TODO: move for-loop print to different function(avoid giant copy-paste)
def listDeck(plr:Player = None, iType:str = '00'):
	#if plr is None -- check only iType of 10, 20, 30, 40, 50, 60; use global deck
	printd("iType = %s" % (iType))
	
	lst = None
	lst2 = None
	prtStr = ""
	if(len(iType) > 2 or len(iType) == 0):
		printd("iType has completely wrong length! Failed to listdeck")
		return False
	elif(len(iType) == 1):
		printd("iType's length is 1. Assuming '0' for 2nd char...")
		iType += '0'
	
	if(plr is None):
		printd("plr is none, not passed probably")
	else:
		printd("plr is not None, player is passed! Checking cards...")
		if(iType[1] == '1'):
			printe("Player %s's unbuilt cards: " %(plr.m_sName))
		else:
			printe("Player %s's cards: " %(plr.m_sName))
	
	if(iType[0] == '0'):
		printd("iType[0] is 0; Calling recursively with specifier '1' and '2'")
		listDeck(plr, '1' + iType[1])
		listDeck(plr, '2' + iType[1])
		return True
	elif(iType[0] == '1'):
		printd("iType[0] is 1; Landmarks...")
		prtStr = "%s Landmarks"
		lst = _LANDMARK_DECK
		if(plr is not None):
			lst2 = plr.m_lLandmarks
	elif(iType[0] == '2'):
		printd("iType[0] is 2; Establishments...")
		prtStr = "%s Establishments"
		lst = _GAMECARD_DECK
		if(plr is not None):
			lst2 = plr.m_lGamecards
	elif(2 < int(iType[0]) < 7):
		printd("iType[0] is %s; %ss..." % (iType[0], GAMECARD_NAMES[int(iType[0])-3]))
		lst = []
		for o in _GAMECARD_DECK:
			if o.m_iGCType == int(iType[0])-3:
				lst.append(o)
		prtStr = "%%s %ss" % (GAMECARD_NAMES[int(iType[0])-3])
		if(plr is not None):
			lst2 = plr.m_lGamecards[int(iType[0])-3]
	else:
		printd("iType[0] value didn't match predefined list! Failed to listdeck")
		return #nothing to do
	
	if(iType[1] == '0'):
		printd('iType[1] is 0;Listing everything!')
		printe('	' + prtStr % ("All"))
		_listDeck(iType[1], lst, lst2)
	elif(iType[1] == '1'):
		printd('iType[1] is 1;Listing unbuilt!')
		printe('	' + prtStr % ("Unbuilt"))
		_listDeck(iType[1], lst, lst2)
	elif(iType[1] == '2'):
		printd('iType[1] is 2;Listing built!')
		printe('	' + prtStr % ("Built"))
		_listDeck(iType[1], lst, lst2)
	else:
		printd("iType[1] value didn't match predefined list! Failed to listdeck")
		return #nothing to do
	return True


