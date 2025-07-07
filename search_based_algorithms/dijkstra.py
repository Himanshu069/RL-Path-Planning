import heapq
import math

def dijkstra(maze, start, goal, dirs=[(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,1),(-1,-1),(1,-1)]):
    H, W = maze.shape
    visited = [[False]*W for _ in range(H)]
    dist = [[float('inf')]*W for _ in range(H)]
    prev = {}
    snapshots = []

    dist[start[0]][start[1]] = 0
    queue = [(0, start)]

    while queue:
        d, current = heapq.heappop(queue)
        if visited[current[0]][current[1]]:
            continue
        visited[current[0]][current[1]] = True
        snapshots.append(current)

        if current == goal:
            break

        for dx, dy in dirs:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and maze[nx][ny] == 0:
                move_cost = math.sqrt(2) if dx != 0 and dy != 0 else 1
                alt = dist[current[0]][current[1]] + move_cost
                if alt < dist[nx][ny]:
                    dist[nx][ny] = alt
                    prev[(nx, ny)] = current
                    heapq.heappush(queue, (alt, (nx, ny)))

    return snapshots, prev

def reconstruct_path(prev, goal):
    path = []
    current = goal
    while current in prev:
        path.append(current)
        current = prev[current]
    path.append(current)
    path.reverse()
    return path