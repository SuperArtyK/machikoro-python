#card ids
#game card = 1
#attractions = 2
#just card = 0

#CARD_TYPE_ID = 0

#temporary, TODO:Move to separate file when creating landmarks
CARD_TYPE_LANDMARK = 2



#card class
#base class of all game cards
class Card:
	#self, card name, card description, card execution type, execution dice roll, is card from advanced set
	def __init__(self, l_sname, l_sdesc, l_itype, l_bHarborExpansion):
		self.m_sName = l_sname
		self.m_sDesc = l_sdesc
		self.m_iType = l_itype
		self.m_bHarborExpansin = l_bHarborExpansion
		self.m_iAmount = 1
		
	def __str__(self):
		return ("Card Title: %s\nDescription: %s" % (self.m_sName, self.m_sDesc))


class LandmarkCard(Card):
	#args: self, (str)name of card, (str)description of card, (int)execution type of card, (list of 2 int) execution dice roll
	def __init__(self, l_sname, l_sdesc, l_idiceRoll, l_bHarborExpansion):
		super(LandmarkCard, self).__init__(l_sname, l_sdesc, CARD_TYPE_LANDMARK, l_bHarborExpansion)
		self.m_iDiceRoll = l_idiceRoll




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






"""