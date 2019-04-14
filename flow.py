import g
import logic
import random

def turn():
	die_result = logic.throw_sticks(random.randint(1,4))
	print "die", die_result
	p_cases = logic.get_player_cases()
	chosen_case = random.randint(0,len(p_cases)-1)
	d_cases = logic.possible_moves(p_cases[chosen_case], die_result)
	destiny = logic.choose_move(d_cases)
	if die_result:
		logic.set_case(p_cases[chosen_case],destiny)
	logic.check_board_integrity()
	g.turn = not g.turn

count = 1
while g.status not in (4,8):
	print "Turn ", count
	turn()
	count+=1
	#raw_input()
	
