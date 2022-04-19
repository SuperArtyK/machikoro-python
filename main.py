

#i guess bad pracice
from player import *



# indicates player number who won, 0 is no-one yet
g_iPlayerWon = 0
	
tmp = CCityHall()
print(tmp)
#print(Card("123", "desc", 1,12))
card = CWheatField();
print(card)
plr = Player("artyk")
plr2 = Player("artyk2")
print(card)
plr.addcard(card)
plr.addcard(card)
card.cardaction(plr)
