
import heapq

# Example Indian city graph (distances in km)
graph = {
    "Delhi": {"Noida": 25, "Gurgaon": 30},
    "Noida": {"Delhi": 25, "Gurgaon": 50, "Faridabad": 40},
    "Gurgaon": {"Delhi": 30, "Noida": 50, "Faridabad": 35},
    "Faridabad": {"Noida": 40, "Gurgaon": 35}
}

def shortest_path(start, end):
    """
    Dijkstra-like shortest path using heapq
    """
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == end:
            return path, cost
        for adj, weight in graph.get(node, {}).items():
            if adj not in visited:
                heapq.heappush(queue, (cost + weight, adj, path))
    return None, float('inf')
