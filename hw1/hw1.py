#!/usr/bin/python3

def search(state, func, params, searchAlg):
	if isGoal(state): return ([],0,0,0)
	fringe = [state]
	explored = 0
	moves = []
	while True:
		node = fringe.pop(searchAlg())
		if isGoal(node):
			# print (node)
			return [x + 1 for x in node['move']], explored, len(fringe), len(moves)
		for param in params:
			if node['move'].count(param) < 2:
				moveStr = ''.join([str(x) for x in sorted(node['move'] + [param])])
				if not moveStr in moves:
					state = func(node, param)
					moves.append(moveStr)
					fringe.append(state)
					explored += 1

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

def main():
	while True:
		state = input('Enter an initial state: ')
		if len(state) == 9 and set(state.lower()) in [{'e'},{'d'},{'r'},{'e','d'},{'e','r'},{'d','r'},{'e','d','r'}]:
			break
		print ('Invalid input.')

	state = {'state': list(state.upper()), 'move': []}
	params = [i for i in range(0,9)]

	moves, expanded, memory, moveHistory = search(state, castSpell, params, bfs)
	print ('Moves: ', moves)
	print ('The number of nodes expanded: ', expanded)
	print ('The number of nodes in fringe: ', memory)
	print ('The number of moves in memory: ', moveHistory)

if __name__ == '__main__':
	main()
