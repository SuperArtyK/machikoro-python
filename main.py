

#i guess bad pracice
from player import *
from eventprint import *



print("Welcome to Machi-koro!\nOriginal game created by Masao Suganuma, port to console by Artemii Kozhemiak.\n")
print("Lines indented with:\n'L ' indicate landmark cards\n'G ' indicate regular game cards\n'C+ ' indicate adding card to player\n'C- ' indicate removing card from player")
printd("And cards with 'C ' indicate cards created with bare class Card()")
print('\n')

# indicates player number who won, 0 is no-one yet
g_iPlayerWon = 0


tmp = [CCityHall(), CHarbor(), CTrainStation(), CShoppingMall(), CAmusementPark(), CRadioTower(), CAirport()]
for o in tmp:
	printe(o)
	print('\n')
print("------------")
#print(Card("123", "desc", 1,12))
card = CWheatField()
printe(card)
plr = Player("artyk")
plr2 = Player("artyk2")
printe(card)
plr.addcard(card)
plr.addcard(card)
plr.addcard(tmp[0])
card.cardaction(plr)
