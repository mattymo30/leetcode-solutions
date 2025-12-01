class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        num_fresh = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                cell = grid[i][j]

                if cell == 1:
                    num_fresh += 1
                if cell == 2:
                    rotten.append((i, j))

        if num_fresh == 0:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0

        while num_fresh != 0:
            time += 1
            step_made_rotten = 0
            new_rotten = []
            for r in rotten:
                for d in directions:
                    adj = (r[0] + d[0], r[1] + d[1])
                    if adj[0] >= 0 and adj[0] < m and adj[1] >= 0 and adj[1] < n:
                        adj_val = grid[adj[0]][adj[1]]

                        if adj_val == 1:
                            step_made_rotten += 1
                            grid[adj[0]][adj[1]] = 2
                            new_rotten.append(adj)
            if step_made_rotten == 0 and num_fresh > 0:
                return -1
            num_fresh -= step_made_rotten
            for r in new_rotten:
                rotten.append(r)
        return time
        
