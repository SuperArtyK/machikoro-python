#i guess bad pracice
from card import *
from cwheat import *
from clandmarks import *

#class of player that posesses the cards themselves
class Player:
    
	def __init__(self, l_sname):
		self.m_sName = l_sname
		#list lists, each sublist indicates GameCard type, such as GCARD_PRIMARY, ~SECONDARY, etc
		#each sublist contains already built cards
		self.m_lCards = [ [], [], [], [] ]
		self.m_iCoins = 3
		#list of bool, landmarks that player have built, as follows(price ascending):
		#City Hall, Harbor, Train Station, Shopping Mall, Amusement Park, Radio Tower, Airport
		#City hall is always built, from start
		self.m_lLandmarks = [True, False, False, False, False, False, False]
		
  
  
	#add card to the list
	#args: self, Card object
	def addcard(self, card):
		print("Entered addcard")
		print("Card is: "+card.m_sName)
		if(card.m_iType == CARD_TYPE_LANDMARK):
			printd("Instance of landmark")
			#TODO: change from 'type() ==' to landmark.id check in m_lLandmarks
			for o in self.m_lLandmarks:
				if(type(o) == type(card)):
					print("You cannot build more than 1 same landmark!")
					return
			self.m_lLandmarks.append(card)
		elif(card.m_iType == CARD_TYPE_GAMECARD):
			printd("Instance of gamecard")
			printd("gamecard type: %d" % (card.m_iGCType))
			#check if card is major, same outcome as landmarks
			for o in self.m_lCards[card.m_iGCType]:
				printd("Checking types; card: %s; cardlist[gctype][i]: %s" % (type(card).__name__, type(o).__name__))
				if(type(o) == type(card)): #match!
					printd("MATCH!")
					if(card.m_iGCType == GCARD_MAJOR):#what if major?
						print("You cannot build more than 1 same Major Establishment!")
					else:
						o.m_iAmount +=1 #increase amount
						printd("Incrementing card amount: %d" % (o.m_iAmount))
					return #return anyway. deed is done
			#oi, looks like we didnt have any cards in list
			#add it quickly!
			printd("Card didn't exist in the list; adding...")
			self.m_lCards[card.m_iGCType].append(card)

