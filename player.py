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
		self.addcard(CCityHall(), True)
		self.addcard(CWheatField(), True)
		
		
	#add card to the list
	#args: self, Card object
	#TODO: Put "adding card" to "buycard"
	def addcard(self, card:Card, bDontCreate = False):
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
				if(type(o) == type(card)): #match!
					printd("Found same card in card list")
					if(card.m_iGCType == GCARD_MAJOR):#what if major?
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
	# 40 -- built gamecards, 41 -- unbuilt gamecards (and so on)
	# 50/51 -- restaurants, 60/61 -- primary, 70/71 -- secondary, 80/81 -- major
	def listcards(self, iType:int = 0):
		printe("Player %s's cards: " %(self.m_sName))
		listdeck(self, iType)
		pass

#args: optional Player type, 
#list deck with possible filters to player
#0 -- all, 10 -- all landmarks, 11 -- unbuilt landmarks, 12 -- built landmarks, 
# 40 -- built gamecards, 41 -- unbuilt gamecards (and so on)
# 50/51 -- restaurants, 60/61 -- primary, 70/71 -- secondary, 80/81 -- major
#TODO: make 0-all call both landmarks and gamecards(recursion)
def listdeck(plr:Player = None, iType = 0):
	#if plr is None -- skip other stuff, just display the deck
	
	printd("entered listdeck")
	if(plr is None):
		printd("plr is none, not passed prob")
		#TODO:Make a cool table
		for i in range(len(_CARD_DECK)):
			#kludge for padding
			#card name + 27-length
			printe("%d: %s;%sActivation: %2d-%d,%sCost:%2d, Type:%s" % 
					(i+1, _CARD_DECK[i].m_sName, ' '*(27-len(_CARD_DECK[i].m_sName)), _CARD_DECK[i].m_lDiceRoll[0], _CARD_DECK[i].m_lDiceRoll[1],
					#now THIS is a kludge. convert number to a string and then calculate it's length
					" "*len(str(_CARD_DECK[i].m_lDiceRoll[1])), 
					_CARD_DECK[i].m_iPrice, _CARD_DECK[i].typeToStr()), MEVENT_GAMECARD)
		for i in range(len(_LANDMARK_DECK)):
			#same kludge here
			#16 - length
			printe("%d: %s;%sCost:%2d, Description: %s" % 
					(i+1, _LANDMARK_DECK[i].m_sName, ' '*(16-len(_LANDMARK_DECK[i].m_sName)), _LANDMARK_DECK[i].m_iPrice, _LANDMARK_DECK[i].m_sShortDesc), MEVENT_LANDMARK)
	else: #else, now play with filtering
		printd("plr is not None, player is passed! Checking his cards...")
		iType
		#good ol' elif tower
		if(iType == 0):
			printe("Landmarks:")
	
