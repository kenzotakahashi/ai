#!/usr/bin/python3

SPACE = 4
COIN = 5

def minimax(state):
	lose = []
	for node in [(minValue(move(state, i)), i) for i in validMoves(state)]:
		if node[0] == 1:
			return ('win', node[1])
		lose.append(node[1])
	# return the move with the least number of coins
	return ('lose', lose[0])
	# return ('lose', min(lose, key=lambda x: x[1]))

def maxValue(state):
	if isEnd(state): return 0 # lose
	return max([minValue(move(state, i)) for i in validMoves(state)])

def minValue(state):
	if isEnd(state): return 1 # win
	return min([maxValue(move(state, i)) for i in validMoves(state)])

def isEnd(state):
	return state[SPACE - 1] == COIN

def move(state, p):
	newState = state[:]
	newState[p[0]] -= p[1]
	newState[p[0] + 1] += p[1]
	return newState

def validMoves(state):
	# i -> space, j-> number of coin
	return [(i, j) for i in range(0, SPACE - 1) for j in range(1, COIN + 1) if state[i] >= j]

def main():
	state = [int(i) for i in input("Enter the board as a comma separated sequence of numbers: ").split(',')]
	if isEnd(state):
		print ('The game is already finished.')
		return

	status = minimax(state)
	print ('Move ' + str(status[1][1]) + ' from space ' + str(status[1][0]+1))
	print ('And you should ' + status[0])


if __name__ == '__main__':
	main()