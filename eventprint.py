#contains code for printing text bound to certain events

#MEvent - machi-koro event
MEVENT_NONE = -1 #''
MEVENT_GENERAL = 0 #'    '
MEVENT_LANDMARK_DESC = 1 # 'LD  '
MEVENT_GAMECARD_DESC = 2 # 'GD  '
MEVENT_CARD_DESC = 3 # 'CD  '
MEVENT_ADD_CARD = 4 # '+C  '
MEVENT_REMOVE_CARD = 5 # '-C  '
MEVENT_ADD_COINS = 6 # '++  '
MEVENT_REMOVE_COINS = 7 # '--  ' 	;pay, to player or to bank
MEVENT_ADD_PLAYER = 8 # '+P  '
MEVENT_LANDMARK = 9 # 'L   '
MEVENT_GAMECARD = 10 # 'G   '
MEVENT_CARD = 11 # 'C   '
MEVENT_ERROR = 12 # '!! ';    error of a PLAYER, not program

#event printing
#args: text string and event type int
def printe(s, e = MEVENT_NONE):
	#replace pattern
	r = ''
	
	if(e == MEVENT_GENERAL):
		r = '    '
	elif(e == MEVENT_LANDMARK_DESC or str(s)[0:15] == "Landmark Title:"):
		r = 'LD  '
	elif(e == MEVENT_GAMECARD_DESC or str(s)[0:16] == "Game Card Title:"):
		r = 'GD  '
	elif(e == MEVENT_CARD_DESC or str(s)[0:11] == "Card Title:"):
		r = 'CD  '
	elif(e == MEVENT_ADD_CARD):
		r = '+C  '
	elif(e == MEVENT_REMOVE_CARD):
		r = '-C  '
	elif(e == MEVENT_ADD_COINS):
		r = '++  '
	elif(e == MEVENT_REMOVE_COINS):
		r = '--  '
	elif(e == MEVENT_ADD_PLAYER):
		r = '+P  '
	elif(e == MEVENT_LANDMARK):
		r = 'L   '
	elif(e == MEVENT_GAMECARD):
		r = 'G   '
	elif(e == MEVENT_CARD):
		r = 'C   '
	elif(e == MEVENT_ERROR):
		r = '!!  '
	
	print((r+str(s)).replace('\n', '\n'+r))

"""
Line prefix legend:

'    ' -- Normal line
'LD  ' -- Detailed description of the landmark card
'GD  ' -- Detailed description of the game card
'CD  ' -- Detailed description of the just the card
'+C  ' -- Adding card to player. EX: when bought
'-C  ' -- Removing card from player, when exchanged
'++  ' -- Player recieves coins
'--  ' -- Player pays with coins
'+P  ' -- Player is added to the game
'L   ' -- Short description of the landmark card
'G   ' -- Short description of the game card
'C   ' -- Short description of the game card
(shown when listing whole card deck or player cards)
'!!  ' -- 


"""