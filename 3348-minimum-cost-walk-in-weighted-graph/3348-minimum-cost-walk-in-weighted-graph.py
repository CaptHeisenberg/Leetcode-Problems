class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        self.Size = [1]*N

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])  # path compression
        return self.root[x]

    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x==y: return False

        if self.Size[x] > self.Size[y]:
            self.Size[x] += self.Size[y]
            self.root[y]=x
        else:
            self.Size[y] += self.Size[x]
            self.root[x]=y
        return True
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph=UnionFind(n)
        cost=[0xFFFFFFFF]*n
        for u, v, w in edges:
            wt=cost[graph.Find(u)] & cost[graph.Find(v)] & w
            graph.Union(u, v)
            rt=graph.Find(u)
            cost[rt]&=wt
        ans=[-1]*(len(query))
        for i, (s, t) in enumerate(query):
            rootS=graph.Find(s)
            if rootS==graph.Find(t):
                ans[i]=cost[rootS]
        return ans
        