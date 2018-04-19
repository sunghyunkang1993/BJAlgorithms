
"""
https://www.acmicpc.net/problem/2631

STRATEGY
Find LIS of the origianl sequence
D =[]
D[i] = LIS from beginning to i

minnumMoves = n - LIS
"""

def findMinNumMoves(n, nums):
	D = [1 for i in range(n)]
	LIS = 0

	for i in range(1, n):
		for j in range(i):
			if nums[i] > nums[j]:
				D[i] = max(D[i], D[j]+1)
				LIS = max(D[i], LIS)

	return n - LIS

if __name__ == "__main__":
	nums = []
	n = int(input())
	for i in range(n):
		nums.append(int(input()))

	print(findMinNumMoves(n, nums))
	