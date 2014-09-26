#!/usr/bin/python3

def search(state, func, params, searchAlg, limit=1000):
	if isGoal(state): return ([],0,0,0)
	searchAlg = searchAlg()
	fringe = [state]
	explored = 0
	moveHistory = []
	while len(fringe) > 0:
		node = fringe.pop(searchAlg)
		if isGoal(node):
			return [x + 1 for x in node['move']], explored, len(fringe), len(moveHistory)
		for param in params:
			if node['move'].count(param) < 2 and len(node['move']) < limit:
				moveStr = ''.join([str(x) for x in sorted(node['move'] + [param])])
				if not moveStr in moveHistory:
					state = func(node, param)
					moveHistory.append(moveStr)
					fringe.append(state)
					explored += 1

	# Failed to find a solution
	return False, explored, 0,0


def ids(state, func, params):
	"""Iterative Deepening"""
	totalExpanded = 0
	limit = 0
	while True:
		# print ('calling search with limit ', limit)
		moves, expanded, memory, moveHistory = search(state, castSpell, params, dfs, limit)
		totalExpanded += expanded
		if moves != False:
			return moves, totalExpanded, memory, moveHistory
		limit += 1

def bfs():
	return 0

def dfs():
	return -1

def isGoal(state):
	return len(set(state['state'])) == 1

def castSpell(state, num):
	newState = state['state'][:]
	for i in createIndex(num):
		newState[i] = 'ERD'['ERD'.index(newState[i]) - 1]
	return {'state': newState, 'move': state['move'] + [num]}

def createIndex(num):
	index = [num]
	if not num in [0,3,6]: index.append(num - 1)
	if not num in [0,1,2]: index.append(num - 3)
	if not num in [2,5,8]: index.append(num + 1)
	if not num in [6,7,8]: index.append(num + 3)
	return index


def initialBoard():
	while True:
		state = input('Enter an initial state: ')
		if len(state) == 9 and set(state.lower()) in [{'e'},{'d'},{'r'},{'e','d'},{'e','r'},{'d','r'},{'e','d','r'}]:
			return state
		print ('Invalid input.')

def chooseAlgorithm():
	while True:
		alg = input('Choose algorithm (breadth first -> [Enter], iterative deepening -> i and [Enter]) ')
		if alg == '' or alg == 'i':
			return alg
		print ('Invalid input.')

def main():
	state = initialBoard()
	algorithm = chooseAlgorithm()

	state = {'state': list(state.upper()), 'move': []}
	params = [i for i in range(0,9)]

	if algorithm == '':
		moves, expanded, memory, moveHistory = search(state, castSpell, params, bfs)
	else:
		moves, expanded, memory, moveHistory = ids(state, castSpell, params)

	print ('Moves: ', moves)
	print ('The number of nodes expanded: ', expanded)
	print ('The number of nodes in fringe: ', memory)
	print ('The number of moves in memory: ', moveHistory)

if __name__ == '__main__':
	main()
