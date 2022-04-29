

#i guess bad pracice
from player import *
from eventprint import *

#TODO:Change in-game phrase 'gamecard' to 'establishment' where possible

print("Welcome to Machi-koro!\nOriginal game created by Masao Suganuma, port to console by Artemii Kozhemiak.\n")
print("Lines indented with:\n'L ' indicate landmark cards\n'G ' indicate regular game cards\n'C+ ' indicate adding card to player\n'C- ' indicate removing card from player")
printd("And cards with 'C ' indicate cards created with bare class Card()")
print('\n')

# indicates player number who won, 0 is no-one yet
g_iPlayerWon = 0


tmp = getLandmarkDeck()
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
plr.addCard(card)
plr.addCard(card)
plr.addCard(tmp[0])
card.cardAction(plr)
print('\n')

#print(plr.hasCard(getLandmarkDeck()[0]))
plr.listCards(2)
print('-----------------')
#listDeck(None, '40')