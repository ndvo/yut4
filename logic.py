import random
import g

def throw_sticks(sticks):
	"""Throw a determined number of sticks"""
	assert sticks <=4
	count = 0
	for i in range(sticks):
		count+=random.randint(0,1)
	return count

def possible_moves(case, die_result):
	"""Returns a list of cases that may be end destination of a piece"""
	possible=[]
	assert die_result <= 4
	if not die_result:
		return [case]
	else:
		fakes = {3:5, 9:6}
		if case == 3 and die_result == 1:
			possible.append(9)
		elif case in fakes:
			fake_sum = fakes[case]+die_result
			possible.append(fake_sum if fake_sum < 9 else fake_sum-8)
		if 0 < case < 9:
			case_sum = case+die_result
			possible.append(case_sum if case_sum < 9 else case_sum-8)
		else:
			possible.append(die_result)
		return possible

def is_friend(destiny):
	"""Returns True if the destiny case is occupied by a friend and False otherwise"""
	if g.board[destiny]:
		if g.board[destiny] <= 4:
			return not g.turn
		else:
			return g.turn
	return False	
		
def set_case(origin, destiny):
	"""Changes the board to conform it to a move"""
	print g.board, origin, g.turn
	assert (g.board[origin] <= 4 and not g.turn) or (g.board[origin] >=5 and g.turn) or (not origin)
	if not origin:
		g.board[origin] = 1 if not g.turn else 5
	if is_friend(destiny):
		g.board[destiny] += int(g.board[origin]) if not g.turn else int(g.board[origin])-4
	else:
		g.board[destiny] = int(g.board[origin])
	g.board[origin]=0
	print g.board, origin, g.turn

def choose_move(moves):
	return moves[0]

def get_player_cases():
	"""Return a list of cases where the player has his pieces"""
	cases = []
	counter = 0
	total = 0
	for i in g.board:
		if i:
			if (i<=4 and not g.turn) or (i>=5 and g.turn):
				total+=i if not g.turn else i-4
				cases.append(counter)
		counter +=1
	if total < 4:
		cases.append(0)
	return cases
		
def board2string():
	to_save = ""
	for i in g.board:
		to_save+=i
	return to_save

def check_board_integrity():
	pieces = [0,0]
	for i in g.board:
		if i and i<=4:
			pieces[0]+=i
		elif i and i>=5:
			pieces[1]+=i-4
	assert pieces[0]<5 and pieces[1]<5
	if g.board[1] in (4,8):
		g.status = g.board[1]

def testing():
	g.board = [0,1,0,2,5,7,0,0,0,0]
	check_board_integrity()
	print g.board, get_player_cases()	
	g.turn = not g.turn
	print g.board, get_player_cases()	
	g.turn = not g.turn
	
	set_case(3,5)
	print g.board
	g.turn = not g.turn
	print g.board, get_player_cases()	
	check_board_integrity()
	

if __name__ == '__main__':
	testing()
