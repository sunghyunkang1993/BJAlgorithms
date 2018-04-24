"""
https://www.acmicpc.net/problem/3020

STRATEGY
Initialize 2 arrays and sort them
obstaclesTop = list of sorted lengths of rocks from the top
obstaclesBot = List of sorted lengths of rocks from the bottom
For each height (from 1 to n)
binary search A and B
find the right most rock that the bug hits,
and the number of obstacles is all the obstacles to the end including that obstacle
number of obstacles in A + number of obstacles in B = totalnumberObstacles
minimumLengthrockA = i+1 (from the top)
minimumLengthrockB = n-i (from the bottom)
"""
def binarysearchIndex(obstacles, target):
	low = 0
	high = len(obstacles) - 1

	while low <= high:
		mid = int((low + high) / 2)
		if obstacles[mid] >= target:
			high = mid - 1
		else:
			low = mid + 1

	return low

def getnumObstacles(obstaclesTop, obstaclesBot, n, lengths):
	minObstacles = lengths
	numOccurences = 0
	obstaclesTop.sort()
	obstaclesBot.sort()

	for height in range(n):
		numOccurencesTop = len(obstaclesTop) - binarysearchIndex(obstaclesTop, height+1)
		numOccurencesBot = len(obstaclesBot) - binarysearchIndex(obstaclesBot, n-height)
		totalObstacles = numOccurencesTop + numOccurencesBot

		if totalObstacles == minObstacles:
			numOccurences += 1
		if totalObstacles < minObstacles:
			minObstacles = totalObstacles
			numOccurences = 1

	return " ".join([str(minObstacles), str(numOccurences)])

if __name__ == "__main__":
	obstaclesTop = []
	obstaclesBot = []
	lengths, height = map(int, input().split())

	for length in range(lengths):
		if length == 0 or length % 2 == 0:
			obstaclesBot.append(int(input()))
		else:
			obstaclesTop.append(int(input()))

	print(getnumObstacles(obstaclesTop, obstaclesBot, height, lengths))
	