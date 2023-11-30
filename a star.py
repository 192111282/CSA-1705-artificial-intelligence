import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_set, closed_set = [], set()
    heapq.heappush(open_set, (0, start, None, 0))  # Add the cost to the heap
    parent = {}

    while open_set:
        f, current, prev, g = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)
        parent[current] = prev

        if current == goal:
            path, node = [], current
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g  # Return the path and its cost

        neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

        for neighbor in neighbors:
            if (
                0 <= neighbor[0] < len(grid[0])
                and 0 <= neighbor[1] < len(grid)
                and grid[neighbor[1]][neighbor[0]] == 0
            ):
                new_g = g + 1
                h = heuristic(neighbor, goal)
                heapq.heappush(open_set, (new_g + h, neighbor, current, new_g))

    return None, None

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)

path, cost = a_star(grid, start, goal)
print("Path:", path if path else "No path found")
print("Path Cost:", cost if cost else "No path found")
