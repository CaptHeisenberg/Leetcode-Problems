
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list for the graph
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False] * n  # Tracks visited nodes
        complete_components = 0  # Count of complete components
        
        for node in range(n):
            if not visited[node]:
                # BFS to find all nodes in the current connected component
                queue = deque([node])
                visited[node] = True
                component = []
                
                while queue:
                    current = queue.popleft()
                    component.append(current)
                    
                    # Explore neighbors
                    for neighbor in adj_list[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Check if the component is complete
                component_size = len(component)
                is_complete = True
                for vertex in component:
                    if len(adj_list[vertex]) != component_size - 1:
                        is_complete = False
                        break  # Early exit if any node fails the check
                
                if is_complete:
                    complete_components += 1
        
        return complete_components