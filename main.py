#i guess bad pracice
from player import *



# indicates player number who won, 0 is no-one yet
g_iPlayerWon = 0

		

#print(Card("123", "desc", 1,12))
card = CWheatField();
plr = Player("artyk")
print(card)
card.cardaction(plr)
print(plr.m_iCoins)
card.m_iID = -1
plr.addcard(card)
plr.addcard(card)
