#!/usr/bin/python3

def bfs(state, func, params):
	if isGoal(state): return True
	fringe = [state]
	explored = []
	states = ''
	moves = []
	while True:
		s = fringe.pop(0)
		for param in params:
			if s['move'].count(param) < 2:
				moveStr = ''.join([str(x) for x in sorted(s['move'] + [param])])
				if not moveStr in moves:
					moves.append(moveStr)
					state = func(s, param)
					# states += (printState(state)) + '\n\n'
					explored.append(state['state'])
					if isGoal(state):
						print (state)
						print (moves)
						# print (fringe)
						# print (explored)
						# print (states)
						return
					fringe.append(state)

					# print (state)

		# print (fringe)
		# print (explored)
		# print (states)

	return True


def isGoal(state):
	return len(set(state['state'])) == 1

def castSpell(state, num):
	newState = state['state'][:]
	for i in createIndex(num):
		newState[i] = changeJewel(newState[i])
	return {'state': newState, 'move': state['move'] + [num]}


def createIndex(num):
	index = [num]
	if not num in [0,3,6]: index.append(num - 1)
	if not num in [0,1,2]: index.append(num - 3)
	if not num in [2,5,8]: index.append(num + 1)
	if not num in [6,7,8]: index.append(num + 3)
	return index

def changeJewel(jewel):
	return 'ERD'['ERD'.index(jewel) - 1]

def printState(state):
	string = ''.join(state['state'])
	return string[0:3] + '\n' + string[3:6] + '\n' + string[6:9]

def main():
	# state = input('enter an initial state: ')
	# state = 'dedeeeded'
	state = 'ededdeddr'
	# state = {'state': list(state.upper()), 'parent': None, 'move': None}
	state = {'state': list(state.upper()), 'move': []}


	params = [i for i in range(0,9)]

	bfs(state, castSpell, params)

	# print(castSpell(state, 4))


	# a = ['R'] * 9
	# for i in range(0,9):
	# 	b = castSpell(a, i)
	# 	printState(b)



if __name__ == '__main__':
	main()