from debugprint import *
#card ids
#game card = 1
#attractions = 2
#just card = 0

#CARD_TYPE_ID = 0


#card class
#base class of all game cards
class Card:
	#self, card name, card description, card execution type, execution dice roll, is card from advanced set
	def __init__(self, l_sname, l_sdesc, l_itype, l_bHarborExpansion, l_iMaxAmount, l_iPrice):
		printd("Creating Card() ->  %s" % (l_sname))
		self.m_sName = l_sname
		self.m_sDesc = l_sdesc
		self.m_iType = l_itype
		self.m_bHarborExpansion = l_bHarborExpansion
		self.m_iAmount = 1
		self.m_iMaxAmount = l_iMaxAmount
		self.m_iPrice = l_iPrice
		
	def __str__(self):
		return ("!Card Title: %s\n!Description: %s\n!From Harbor Expansion: %r" % (self.m_sName, self.m_sDesc, self.m_bHarborExpansion))









"""Turn idea: first we throw dice and check the value.
Then we filter the cards to an active card list, same structure as normal list.
Filtering: main player filters all cards to be used, other players filter only restaurants and primary
We execute function 'payplayer' of each other player, passing main player as arg. order: reverse turn order
to pay the players
if main player has 0 coins, skip paying players and start recieving
Order: same as turn order(doesnt matter!)
then we prompt to buy cards. Display previously bought card and how much left. Display current coin amount

Commands: 

show(any time): list of all cards and their status, all game cards, all landmarks,
all unbuilt cards, unbuilt game cards, unbuilt landmarks, each opponents' cards, 
1 opponent's cards, unbuilt cards/gamecards/landmarks of opponent,
coin amount of active player, coin amount of 1/each opponent, dice roll amount

roll the dice: roll 1 die, roll 2 dice, remember dice rolling amount, auto-roll

buy: buy card, buy landmark, buy gamecard; by name/number(previous list)



Allow user to disable commands and use forced action order




"""