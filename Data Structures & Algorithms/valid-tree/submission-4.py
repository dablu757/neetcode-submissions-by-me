class Dsu:
    def __init__(self, n: int):
        self.size = [1]*n
        self.parent = [i for i in range(n)]


    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        
        return self.parent[x]

    
    def union(self,a: int, b: int):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return False

        else:
            size_a = self.size[parent_a]
            size_b = self.size[parent_b]

            if size_a < size_b:
                self.parent[parent_a]=parent_b
                self.size[parent_b]+=size_a

            else:
                self.parent[parent_b]=parent_a
                self.size[parent_a]+=size_b
            
            return True

  
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = [[] for _ in range(n)]
        if len(edges)!=n-1:
            return False

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for neighbour in graph[node]:

                if neighbour == parent:
                    continue

                if neighbour in visited:
                    return False

                if not dfs(neighbour, node):
                    return False

            return True

        # def dfs(node,parent):
        #     visited.add(node)

        #     for neighbour in graph[node]:
        #         if neighbour not in visited and dfs(neighbour,node):
        #             return True
                
        #         elif neighbour in visited and neighbour!=parent:
        #             return True

        #     return False

        
        if not dfs(0,-1):
            return False
        
        return len(visited)==n

        # dsu = Dsu(n)

        # if len(edges)!=n-1:
        #     return False

        # for u,v in edges:
        #     if not dsu.union(u,v):
        #         return False
        # return True












        