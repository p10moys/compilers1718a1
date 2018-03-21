
def getchar(words,pos):
        """ returns char at pos of words, or None if out of bounds """

        if pos<0 or pos>=len(words): return None
        elif words[pos]=='0' or words[pos]=='1': return '0-1'
        elif words[pos]=='4' or words[pos]=='5': return '4-5'
        elif words[pos]==':' or words[pos]=='.': return ':'
        elif words[pos]<='6' or words[pos]>='9': return '6-9'
        
        else: return words[pos]

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

# Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων...
td = { 'q0':{ '0-1':'q1','2':'q2','3':'q3','4-5':'q3','6-9':'q3' },
       'q1':{ '0-1':'q3','2':'q3','3':'q3','4-5':'q3','6-9':'q3',':':'q4' },
       'q2':{ '0-1':'q3','2':'q3','3':'q3',':':'q4' },
       'q3':{ ':':'q4' },
       'q4':{ '0-1':'q5','2':'q5','3':'q5','4-5':'q5' },
       'q5':{ '0-1':'q6','2':'q6','3':'q6','4-5':'q6','6-9':'q6' }
     } 

# the dictionary of accepting states and their
# corresponding token

# Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής...
ad = { 'q6':'TIME_TOKEN'
     }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
	
