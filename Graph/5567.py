"""
https://www.acmicpc.net/problem/5567

STRATEGY
Initialize graph as a node and list of vertices
Maintain a set of visited nodes
Iterate 1's nodes vertices and if not in set, increment number
"""
def getNumofFriends(friends_map):
	numFriends = 0
	visited = set()
	for friend in friends_map[1]:
		if friend not in visited:
			visited.add(friend)
			numFriends += 1

		for friendOfFriend in friends_map[friend]:
			if friendOfFriend not in visited:
				visited.add(friendOfFriend)
				numFriends += 1
	return numFriends



if __name__ == "__main__":
	friends_map = {}
	n = int(input())
	m = int(input())
	for i in range(m):
		node, vertex = map(int, input().split())
		if node in friends_map:
			friends_map[node].append(vertex)
		else:
			friends_map[node] = [vertex]

	print(getNumofFriends(friends_map))


