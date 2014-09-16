#!/usr/bin/python3

def bfs(state, func, params):
	if isGoal(state): return True
	fringe = [state]
	explored = []
	moves = []
	while True:
		s = fringe.pop(0)
		for param in params:
			if s['move'].count(param) < 2:
				moveStr = ''.join([str(x) for x in sorted(s['move'] + [param])])
				if not moveStr in moves:
					moves.append(moveStr)
					state = func(s, param)
					explored.append(state['state'])
					if isGoal(state):
						print (state)
						print ('The number of nodes expanded: ', len(explored))
						print ('The number of nodes in fringe: ', len(fringe))
						return
					fringe.append(state)
	return


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
	while True:
		state = input('Enter an initial state: ')
		if len(state) == 9 and set(state.lower()) in [{'e'},{'d'},{'r'},{'e','d'},{'e','r'},{'d','r'},{'e','d','r'}]:
			break
		print ('Invalid input.')

	state = {'state': list(state.upper()), 'move': []}


	params = [i for i in range(0,9)]

	bfs(state, castSpell, params)


	# a = ['R'] * 9
	# for i in range(0,9):
	# 	b = castSpell(a, i)
	# 	printState(b)



if __name__ == '__main__':
	main()


#'edreddree' 9 moves