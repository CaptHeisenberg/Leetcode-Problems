struct UnionFind {
    root: Vec<usize>,
    weight: Vec<i32>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            root: (0..n).collect(),
            weight: vec![i32::MAX; n],
        }
    }

    fn find(&mut self, a: usize) -> usize {
        if self.root[a] == a {
            return self.root[a];
        }

        self.root[a] = self.find(self.root[a]);

        self.root[a]
    }

    fn union(&mut self, a: usize, b: usize, w: i32) {
        let a = self.find(a);
        let b = self.find(b);

        let w = self.weight[a] & self.weight[b] & w;

        self.weight[a] = w;
        self.weight[b] = w;

        if a != b {
            self.root[b] = a;
        }
    }

    fn query(&mut self, a: usize, b: usize) -> i32 {
        match (self.find(a), self.find(b)) {
            (a, b) if a == b => self.weight[a],
            _ => -1,
        }
    }
}

impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let mut uf = UnionFind::new(n as usize);

        for edge in edges {
            uf.union(edge[0] as usize, edge[1] as usize, edge[2]);
        }

        query
            .into_iter()
            .map(|q| uf.query(q[0] as usize, q[1] as usize))
            .collect()
    }
}
