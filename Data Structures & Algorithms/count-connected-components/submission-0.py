class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()

        def dfs(node):

            visited.add(node)

            for neighbore in graph[node]:
                if neighbore not in visited:
                    dfs(neighbore)
            
        
        res = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res
        