#i guess bad pracice
from player import *



# indicates player number who won, 0 is no-one yet
g_iPlayerWon = 0
	
tmp = CLandmark("tmp", "tmp", False, 10)
print(tmp)
#print(Card("123", "desc", 1,12))
card = CWheatField();
plr = Player("artyk")
print(card)
plr.addcard(card)
card.cardaction(plr)
