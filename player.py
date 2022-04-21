#contains class of player that posesses the cards themselves

#i guess bad pracice
from card import *
from cwheat import *
from clandmarks import *
from eventprint import *

#internal use only: player count
_PLAYER_COUNT = 0
#internal use only: deck of all cards in the game
_CARD_DECK = [CWheatField()]
_LANDMARK_DECK = [CCityHall(), CHarbor(), CTrainStation(), CShoppingMall(), CAmusementPark(), CRadioTower(), CAirport()]

def getLandmarkDeck():
	return _LANDMARK_DECK

def getGamecardDeck():
	return _LANDMARK_DECK



#class itself
class Player:
    #constructor
	def __init__(self, l_sName):
		self.m_sName = l_sName
		global _PLAYER_COUNT
		_PLAYER_COUNT +=1
		printe("Player %s has entered the game! (Total: %d players)" % (self.m_sName, _PLAYER_COUNT), MEVENT_ADD_PLAYER)
		#list lists, each sublist indicates GameCard type, such as GCARD_PRIMARY, ~SECONDARY, etc
		#each sublist contains already built cards
		self.m_lCards = [ [], [], [], [] ]
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
			for o in self.m_lLandmarks:
				if(o.m_iID == card.m_iID):
					printe("You cannot build more than 1 same landmark!", MEVENT_ERROR)
					return
			if(bDontCreate):
				self.m_lLandmarks.append(card)
			else:
				self.m_lLandmarks.append(card.__class__())
		elif(card.m_iType == CARD_TYPE_GAMECARD):
			printd("Instance of gamecard" + card.typeToStr())
			#check if card is major, same outcome as landmarks
			for o in self.m_lCards[card.m_iGCType]:
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
				self.m_lCards[card.m_iGCType].append(card)
			else:
				self.m_lCards[card.m_iGCType].append(card.__class__())


	#lists cards of a player with optional filter applied
	#args: type of cards to display:
	#0 -- all, 10 -- all landmarks, 11 -- unbuilt landmarks, 12 -- built landmarks, 
	# 20 -- all built gamecards(+status built/unbuilt), 21 -- unbuilt gamecards, 22 -- built gamecards
	# 30/31/32 -- restaurants, 40/41/42 -- primary, 50/51/52 -- secondary, 60/61/62 -- major
	def listCards(self, iType = 0):
		iType = str(iType)
		if(len(iType) == 2 and iType[1] == '1'):
			printe("Player %s's unbuilt cards: " %(self.m_sName))
		else:
			printe("Player %s's cards: " %(self.m_sName))
		listDeck(self, iType)
		pass
	
	def hasCard(self, card:Card):
		for i in self.m_lCards:
			for o in i:
				if(type(card) is type(o)):
					return True
		for o in self.m_lLandmarks:
			if(type(card) is type(o)):
				return True
		return False
	

#args: optional Player type, 
#list deck with possible filters to player
#0 -- all, 10 -- all landmarks, 11 -- unbuilt landmarks, 12 -- built landmarks, 
# 20 -- all built gamecards(+status built/unbuilt), 21 -- unbuilt gamecards, 22 -- built gamecards
# 30/31/32 -- restaurants, 40/41/42 -- primary, 50/51/52 -- secondary, 60/61/62 -- major
#TODO: print error if iType is wrong
def listDeck(plr:Player = None, iType = 0):
	#if plr is None -- check only iType of 10, 20, 30, 40, 50, 60; use global deck
	iType = str(iType)
	printd("entered listdeck")
	printd("iType = %s" % (iType))
	if(plr is None):
		printd("plr is none, not passed probably")
		#TODO:Make a cool-looking table
		if(iType[0] == '0'):
			listDeck(None, 10)
			listDeck(None, 20)
		elif(iType == '10'):
			printe("Landmarks:", MEVENT_GENERAL)
			for i in range(len(_LANDMARK_DECK)):
				#same kludge here
				#16 - length
				printe("%2d: %s;%sCost:%2d, Description: %s" % 
						(i+1, _LANDMARK_DECK[i].m_sName, ' '*(16-len(_LANDMARK_DECK[i].m_sName)), _LANDMARK_DECK[i].m_iPrice, _LANDMARK_DECK[i].m_sShortDesc), MEVENT_LANDMARK)
		elif(iType == '20'):
			printe("Establishments:", MEVENT_GENERAL)
			for i in range(len(_CARD_DECK)):
				#kludge for padding
				#card name + 27-length
				printe("%2d: %s;%sActivation:%2d-%d,%sCost:%2d, Type:%s Description: %s" % 
						(i+1, _CARD_DECK[i].m_sName, ' '*(27-len(_CARD_DECK[i].m_sName)), _CARD_DECK[i].m_lDiceRoll[0], _CARD_DECK[i].m_lDiceRoll[1],
						#now THIS is a kludge. convert number to a string and then calculate it's length
						" "*len(str(_CARD_DECK[i].m_lDiceRoll[1])), 
						_CARD_DECK[i].m_iPrice, _CARD_DECK[i].typeToStr(), _CARD_DECK[i].m_sShortDesc), MEVENT_GAMECARD)
		#establishments
		elif(iType == '30' or iType == '40' or iType == '50' or iType == '60'):
			#since game card id's are from 0 to 3, we can just convert iType to int and check
			printe(GAMECARD_NAMES[int(iType[0])-3]+"s:", MEVENT_GENERAL)
			for i in range(len(_CARD_DECK)):
				if(_CARD_DECK[i].m_iGCType == (int(iType[0])-3)):
					#kludge for padding
					#card name + 27-length
					printe("%2d: %s;%sActivation:%2d-%d,%sCost:%2d, Type:%s Description: %s" % 
							(i+1, _CARD_DECK[i].m_sName, ' '*(27-len(_CARD_DECK[i].m_sName)), _CARD_DECK[i].m_lDiceRoll[0], _CARD_DECK[i].m_lDiceRoll[1],
							#now THIS is a kludge. convert number to a string and then calculate it's length
							" "*len(str(_CARD_DECK[i].m_lDiceRoll[1])), 
							_CARD_DECK[i].m_iPrice, _CARD_DECK[i].typeToStr(), _CARD_DECK[i].m_sShortDesc), MEVENT_GAMECARD)
	else: #else, now play with filtering
		printd("plr is not None, player is passed! Checking cards...")
		
		#good ol' elif tower
		if(iType[0] == '0'): #all cards
			listDeck(plr, "10")
			listDeck(plr, "20")
		elif(iType[0] == '1'): #landmarks
			if(iType[1] == '0'): #all cards
				printe("Landmarks:", MEVENT_GENERAL)
				for i in range(len(_LANDMARK_DECK)):
					#same kludge here
					#16 - length
					printe("%2d: %sbuilt) %s;%sCost:%2d, Description: %s" % 
							(i+1, '  (' if(plr.hasCard(_LANDMARK_DECK[i])) else '(un',_LANDMARK_DECK[i].m_sName, ' '*(16-len(_LANDMARK_DECK[i].m_sName)), _LANDMARK_DECK[i].m_iPrice, _LANDMARK_DECK[i].m_sShortDesc), MEVENT_LANDMARK)
			elif(iType[1] == '1'): #unbuilt cards
				printe("Unbuilt Landmarks:", MEVENT_GENERAL)
				for i in range(len(_LANDMARK_DECK)):
					if(not plr.hasCard(_LANDMARK_DECK[i])):
						#same kludge here
						#16 - length
						printe("%2d: %s;%sCost:%2d, Description: %s" % 
								(i+1, _LANDMARK_DECK[i].m_sName, ' '*(16-len(_LANDMARK_DECK[i].m_sName)), _LANDMARK_DECK[i].m_iPrice, _LANDMARK_DECK[i].m_sShortDesc), MEVENT_LANDMARK)
					elif(i == (len(_LANDMARK_DECK) -1)):
						printe(" 0: None", MEVENT_LANDMARK)
			elif(iType[1] == '2'): #built cards
				printe("Built Landmarks:", MEVENT_GENERAL)
				for i in range(len(plr.m_lLandmarks)):
					#same kludge here
					#16 - length
					printe("%2d: %s;%sCost:%2d, Description: %s" % 
							(i+1, plr.m_lLandmarks[i].m_sName, ' '*(16-len(plr.m_lLandmarks[i].m_sName)), plr.m_lLandmarks[i].m_iPrice, plr.m_lLandmarks[i].m_sShortDesc), MEVENT_LANDMARK)
		elif(iType[0] == '2'): #all gamecards
			if(iType[1] == '0'): #all cards
				printe("Establisments:", MEVENT_GENERAL)
				for i in range(len(_CARD_DECK)):
					#kludge for padding
					#card name + 27-length
					printe("%2d: %sbuilt) %s;%sActivation:%2d-%d,%sCost:%2d, Type:%s, Description: %s" % 
							(i+1,'  (' if(plr.hasCard(_CARD_DECK[i])) else '(un', _CARD_DECK[i].m_sName, ' '*(27-len(_CARD_DECK[i].m_sName)), _CARD_DECK[i].m_lDiceRoll[0], _CARD_DECK[i].m_lDiceRoll[1],
							#now THIS is a kludge. convert number to a string and then calculate it's length
							" "*(3-len(str(_CARD_DECK[i].m_lDiceRoll[1]))), 
							_CARD_DECK[i].m_iPrice, _CARD_DECK[i].typeToStr(), _CARD_DECK[i].m_sShortDesc), MEVENT_GAMECARD)
			elif(iType[1] == '1'): #unbuilt cards
				printe("Unbuilt Establisments:", MEVENT_GENERAL)
				for i in range(len(_CARD_DECK)):
					#kludge for padding
					#card name + 27-length
					if(not plr.hasCard(_CARD_DECK[i])):
						printe("%2d: %s;%sActivation:%2d-%d,%sCost:%2d, Type:%s Description: %s" % 
								(i+1, _CARD_DECK[i].m_sName, ' '*(27-len(_CARD_DECK[i].m_sName)), _CARD_DECK[i].m_lDiceRoll[0], _CARD_DECK[i].m_lDiceRoll[1],
								#now THIS is a kludge. convert number to a string and then calculate it's length
								" "*len(str(_CARD_DECK[i].m_lDiceRoll[1])), 
								_CARD_DECK[i].m_iPrice, _CARD_DECK[i].typeToStr(), _CARD_DECK[i].m_sShortDesc), MEVENT_GAMECARD)
					elif(i == (len(_CARD_DECK) -1)):
						printe(" 0: None", MEVENT_GAMECARD)
			elif(iType[1] == '2'):
				printe("Built Establisments:", MEVENT_GENERAL)
				for o in range(len(plr.m_lCards)):
					printe("	" + GAMECARD_NAMES[o]+"s:")
					if(len(plr.m_lCards[o]) == 0):
						printe(" 0: None", MEVENT_GAMECARD)
						continue
					for i in range(len(plr.m_lCards[o])):
						printe("%2d: %s;%sActivation:%2d-%d,%sCost:%2d, Type:%s Description: %s" % 
								(i+1, plr.m_lCards[o][i].m_sName, ' '*(27-len(plr.m_lCards[o][i].m_sName)), plr.m_lCards[o][i].m_lDiceRoll[0], plr.m_lCards[o][i].m_lDiceRoll[1],
								#now THIS is a kludge. convert number to a string and then calculate it's length
								" "*len(str(plr.m_lCards[o][i].m_lDiceRoll[1])), 
								plr.m_lCards[o][i].m_iPrice, plr.m_lCards[o][i].typeToStr(), plr.m_lCards[o][i].m_sShortDesc), MEVENT_GAMECARD)
					

			
