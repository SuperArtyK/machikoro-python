#contains code for printing text bound to certain events

#MEvent - machi-koro event
MEVENT_NONE = -1
MEVENT_GENERAL = 0
MEVENT_LANDMARK_DESC = 1
MEVENT_GAMECARD_DESC = 2
MEVENT_CARD_DESC = 3
MEVENT_ADD_CARD = 4
MEVENT_REMOVE_CARD = 5
MEVENT_ADD_COINS = 6
MEVENT_REMOVE_COINS = 7 #pay, to player or to bank
MEVENT_ADD_PLAYER = 8
MEVENT_LANDMARK = 9
MEVENT_GAMECARD = 10
MEVENT_CARD = 11
MEVENT_ERROR = 12 #error of PLAYER, not program

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
		r = '!!   '
	else:
		r = ''
	
	print((r+str(s)).replace('\n', '\n'+r))