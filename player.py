#i guess bad pracice
from card import *
from cwheat import *
from clandmarks import *
from eventprint import *

#class of player that posesses the cards themselves

_PLAYER_COUNT = 0


_CARD_DECK = [CWheatField()]

class Player:
    
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

	#args: type of cards to display
	#0 -- all, 10 -- all landmarks, 11 -- unbuilt landmarks, 12 -- built landmarks, 
	# 40 -- built gamecards, 41 -- unbuilt gamecards (and so on)
	# 50/51 -- restaurants, 60/61 -- primary, 70/71 -- secondary, 80/81 -- major
	#TODO: make 0-all call both landmarks and gamecards(recursion)
	def listcards(self, iType = 0, bIntro = True):
		global _CARD_DECK
		if(bIntro):
			print("Player %s's " % (self.m_sName), end='')
		pass

