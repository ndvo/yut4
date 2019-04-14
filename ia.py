import logic
import random

def choose_sticks(cases):
	#TODO: return chosen number of sticks
	## set desirable number
	## set the worst number
	## if worst may be avoided even if it is the result, try desirable
	## else avoid worst, try desirable
	pass


def choose_move():
	#TODO: chose a play
	#Can I win now?
	#Can he win next?
	#Can I avoid being beaten by merging in shortcut?
	#Can I merge or beat in a shortcut?
	#Can I avoid being beaten by merging?
	#Can I take a shortcut?
	#Double beat?
	#Can I avoid?
	##What avoid?
	#Can I beat?
	## What beat?
	#Can I merge?
	## What merge?
	cases = logic.get_player_cases()
	choose_sticks(cases)

	def possible_moves(case, die_result):
	for i in cases 

def avoid(case):
	to_avoid = []
	opponent_cases = logic.get_player_cases(player=opponent)
	for i in opponent_cases:
		to_avoid=to_avoid+[i+1,i+2]
	return avoid

def beat():
	return logic.get_player_cases(player=opponent)
