from collections import deque
def nextMove(n, r, c, grid):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # LEFT, RIGHT, UP, DOWN
    visited = set()
    queue = deque([(r, c)])
    
    while queue:
        row, col = queue.popleft()
        if grid[row][col] == 'p':
            return get_direction(r, c, row, col)
        
        visited.add((row, col))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
    
    return ""

def get_direction(bot_r, bot_c, princess_r, princess_c):
    if bot_r > princess_r:
        return "UP"
    elif bot_r < princess_r:
        return "DOWN"
    elif bot_c > princess_c:
        return "LEFT"
    elif bot_c < princess_c:
        return "RIGHT"

# Parse input
n = int(input())
r, c = map(int, input().strip().split())
grid = [input() for _ in range(n)]

print(nextMove(n, r, c, grid))
