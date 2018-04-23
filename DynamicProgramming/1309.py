"""
https://www.acmicpc.net/problem/1309

STRATEGY
D[i][0] = number of ways to place lions when not plaing a lion on i'th row
D[i][1] = number of ways to place lions when a lion on left of i'th row
D[i][1] = number of ways to place lions when a lion on right of i'th row

D[i][0] = D[i-1][0] + D[i-1][1] + D[i-1][2]
D[i][1] = D[i-1][0] + D[i-1][2]
D[i][2] = D[i-1][0] + D[i-1][1]
"""

def getNumPlacements(n):
	D = [[0 for col in range(3)] for row in range(n)]
	D[0][0] = D[0][1] = D[0][2] = 1

	for row in range(1, n):
		D[row][0] = (D[row-1][0] + D[row-1][1] + D[row-1][2]) % 9901
		D[row][1] = (D[row-1][0] + D[row-1][2]) % 9901
		D[row][2] = (D[row-1][0] + D[row-1][1]) % 9901

	return (D[n-1][0] + D[n-1][1] + D[n-1][2]) % 9901


if __name__ == "__main__":
	n = int(input())
	print(getNumPlacements(n))
