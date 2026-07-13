class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        parent=[i for i in range(n)]
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        def union(u, v):
            pa=find(u)
            pb=find(v)
            if pa!=pb:
                parent[pb]=pa
            else:
                return True
        for u, v in edges:
            if union(u, v):
                return False
        return True