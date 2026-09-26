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
                self.size[b]+=size_a

            else:
                self.parent[parent_b]=parent_a
                self.size[a]+=size_b
            
            return True

    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = Dsu(n)

        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return True












        