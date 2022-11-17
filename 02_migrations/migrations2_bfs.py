import collections

def bfs(grid, start, height, width, wall = '#', goal = '*'):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            path_new = [(e[1], e[0]) for e in path]
            return path_new
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return []
               
            
def fill_criteria_L(grid, start, L):
    i_start = start[0]
    return [e if abs(i_start - idx) <= L else '#'*len(e) for idx, e in enumerate(grid)]


def insert_destication(grid, end, L):
    grid2 = grid.copy()
    grid2[end[0]] = ''.join([e if idx != end[1] else "*" for idx, e in enumerate(grid2[end[0]])])
    return grid2


def check_reachable(mat, start, end, L, height, width):
    new_start = (start[1], start[0])
    
    mat2 = insert_destication(mat, end, L)
    grid = fill_criteria_L(mat2, start, L)
    
    path = bfs(grid, new_start, height, width)
    return int(len(path)!=0)
    

if __name__ == "__main__":
    h, w, num = list(map(int, input().split(" ")))
    mat = [input() for i in range(h)]
    list_input_check = [input() for i in range(num)]
    
    list_reachable = []
    for input_check in list_input_check:
        i1, j1, i2, j2, L = [int(e) for e in input_check.split(' ')]
        start = (i1-1, j1-1)
        end = (i2-1, j2-1)
        
        hasPath = check_reachable(mat, start, end, L, h, w)
        
        list_reachable.append(hasPath)
        print(hasPath)