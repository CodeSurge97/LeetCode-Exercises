 def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        if n < 2:
            return True
    
        visited = [False] * n
        color = [0] * n
    
        for i in range(n - 2):
    
            if visited[i]:
                continue
            q = []
            q.append(i)

            color[i] = 1
            visited[i] = True
        
            while len(q) > 0:
                node = q.pop()
                for child in graph[node]:
                    if color[child] == color[node]:
                        return False
                    if not visited[child]:
                        visited[child] = True
                    # Mark visited before visiting its children in queue
                    # to avoid multiple insertion of same node
                        color[child] = -color[node]
                        q.append(child) 
        return True