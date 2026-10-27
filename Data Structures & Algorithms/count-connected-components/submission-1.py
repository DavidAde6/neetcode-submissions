class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # start at 0
        # explore every neighbour at it to an explored set
        # to explore a neighbuor get a nodes connection, add it to explored. 
        # once one isn't in there, increment count

        count = 0
        explored = set()
        #edgeMap = {key: value for key, value in edges}

        edgeMap = {}
        for i, j in edges:
            if i not in edgeMap:
                edgeMap[i] = []
            if j not in edgeMap:
                edgeMap[j] = []
            edgeMap[i].append(j)
            edgeMap[j].append(i)

        # need to loop in 

        def dfs(index):
            if index in explored or index not in edgeMap:
                return

            explored.add(index)

            for i in edgeMap[index]:
                dfs(i)

        res = 0
        for i in range(n):
            if i not in explored:
                res += 1
                dfs(i)
        
        return res