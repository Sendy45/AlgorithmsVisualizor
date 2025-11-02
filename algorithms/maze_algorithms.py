from visualization import render_frame, Cell, Maze
from random import choice, shuffle
from heapq import heappush, heappop

# Made non recursive to prevent max recursion limit
def depth_first_search_generation(maze: Maze, start: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:

    if start is None:
        start = maze.get_cell(0, 0)

    start.visited = True
    stack = [start]

    while stack:
        current = stack[-1]
        neighbors = [n for n in maze.get_neighbors(current) if not n.visited]

        if neighbors:
            neighbor = choice(neighbors)
            current.del_walls(neighbor)
            neighbor.visited = True
            stack.append(neighbor)
        else:
            stack.pop()

        render_frame([maze], delay) if visualize else None

    maze.clean_all()

    return maze

def prims_simple_generation(maze: Maze, start: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze:
    if start is None:
        start = maze.get_cell(0, 0)

    start.visited = True
    cells = [start]

    while cells:
        render_frame([maze], delay) if visualize else None

        # Pick a random visited cell
        cell = choice(cells)
        unvisited_neighbors = [n for n in maze.get_neighbors(cell) if not n.visited]

        if unvisited_neighbors:
            neighbor = choice(unvisited_neighbors)
            cell.del_walls(neighbor)
            neighbor.visited = True
            cells.append(neighbor)
        else:
            # No unvisited neighbors, remove cell
            cells.remove(cell)

    maze.clean_all()

    return maze

def prims_cell_based_generation(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze:
    if current is None:
        current = maze.get_cell(0, 0)

    current.visited = True
    frontiers = maze.get_neighbors(current)

    while frontiers:
        render_frame([maze], delay) if visualize else None

        # Pick a random frontier cell
        current = choice(frontiers)
        frontiers.remove(current)

        # Find visited neighbors
        visited_neighbors = [n for n in maze.get_neighbors(current) if n.visited]

        if visited_neighbors:
            neighbor = choice(visited_neighbors)
            current.del_walls(neighbor)
            current.visited = True

            # Add its unvisited neighbors to frontier
            for next_neighbor in maze.get_neighbors(current):
                if not next_neighbor.visited and next_neighbor not in frontiers:
                    frontiers.append(next_neighbor)

    maze.clean_all()

    return maze

def kruskal_generation(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze:
    if current is None:
        current = maze.get_cell(0, 0)

    cells = maze.all_cells()

    # Divides cells into sets, each set is assigned to its original cell - the parent
    # Set - each cell in the set is reachable from any other cell in the set
    # When all the cells has the same parent - maze in finished
    parent = {cell: cell for cell in cells}
    components = len(cells) # number of disjoint sets

    # Find the parent of a given cell
    def find(cell: Cell) -> Cell:
        if parent[cell] != cell: # find the root
            parent[cell] = find(parent[cell]) # Recursively gets the cell's parent until finding the root
        return parent[cell] # Return the root

    # Merge two sets - puts both under the same parent (root)
    def union(a: Cell, b: Cell) -> None:
        nonlocal components
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_a] = root_b # merge sets
            components -= 1  # one less disjoint set

    current.visited = True

    # Create edges list
    # Using set to prevent duplicates
    edges = set()
    for cell in cells:
        for neighbor in maze.get_neighbors(cell):
            edge = tuple(sorted([cell, neighbor], key=lambda c: (c.row, c.col))) # prevent same edge in a different form - (a, b) == (b, a)
            edges.add(edge)

    edges = list(edges)
    shuffle(edges)

    # Check every edge until no more left or all cells connected
    for cell_a, cell_b in edges:
        render_frame([maze], delay) if visualize else None

        # Edge divides cells that cant reach each other
        if find(cell_a) != find(cell_b):
            cell_a.del_walls(cell_b) # Delete edge
            cell_a.visited = True
            cell_b.visited = True
            union(cell_a, cell_b) # Merge sets

        # Early break: all cells connected
        if components == 1:
            break

    maze.clean_all()

    return maze



def right_wall_follower(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    if current is None:
        current = maze.get_cell(0, 0)
    direction = 1  # Start facing RIGHT
    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)

    while current != goal:
        current.highlight()
        current.visited = True
        render_frame([maze], delay) if visualize else None

        # Determine the direction indices for walls
        RIGHT, FRONT, LEFT = (direction + 1) % 4, direction, (direction - 1) % 4

        # Check walls relative to current direction
        right_wall = current.walls[RIGHT]
        front_wall = current.walls[FRONT]

        if not right_wall:
            # Turn right and move forward
            direction = RIGHT
            next_cell = maze.get_next_cell(current, direction)
            if next_cell is not None:
                current.unhighlight()
                current = next_cell
        elif not front_wall:
            # Move forward
            next_cell = maze.get_next_cell(current, FRONT)
            if next_cell is not None:
                current.unhighlight()
                current = next_cell
        else:
            # Turn left (or turn around if blocked)
            direction = LEFT

    current.highlight()
    current.visited = True
    render_frame([maze], delay) if visualize else None

    return maze

def dead_end_filling(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    if current is None:
        current = maze.get_cell(0, 0)

    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)

    cells = maze.all_cells()
    dead_ends = []

    for cell in cells:
        if cell == goal or cell == current:
            continue

        neighbors = maze.navigable_neighbors(cell)
        if len(neighbors) == 1:
            cell.visited = True
            dead_ends.append(neighbors[0])

    render_frame([maze], delay) if visualize else None

    while dead_ends:
        new_dead_end = []
        for cell in dead_ends:

            if cell == goal or cell == current:
                continue

            # If this cell is now a dead end (only one open neighbor not yet filled)
            neighbors = maze.navigable_unvisited_neighbors(cell)
            if len(neighbors) == 1:
                cell.visited = True
                new_dead_end.append(neighbors[0])

        dead_ends = new_dead_end # Replace with new list (preventing modifying a list while iterating)
        render_frame([maze], delay) if visualize else None

    # Follow the only remaining path from start to end - the solution
    while current != goal:
        current.highlight()
        current.visited = True
        render_frame([maze], delay) if visualize else None

        unvisited_neighbors = maze.navigable_unvisited_neighbors(current)

        if not unvisited_neighbors:
            break  # safety check — prevents IndexError

        current = unvisited_neighbors[0]

    current.highlight()
    render_frame([maze], delay) if visualize else None

    return maze

def dijkstra(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    if current is None:
        current = maze.get_cell(0, 0)

    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)
    start = current # for later backtracking

    current.visited = True
    render_frame([maze], delay) if visualize else None

    distances = {cell: float("inf") for cell in maze.all_cells()}
    current_distance = 0

    distances[current] = current_distance
    neighbors = maze.navigable_neighbors(current)

    while current != goal:
        current_distance += 1
        next_neighbors = []
        for neighbor in neighbors:
            neighbor.visited = True

            distances[neighbor] = current_distance

            # Add all unvisited, navigable neighbors of this neighbor
            for n in maze.navigable_neighbors(neighbor):
                if not n.visited and n not in next_neighbors:
                    next_neighbors.append(n)

            if neighbor == goal:
                current = neighbor

        neighbors = next_neighbors
        render_frame([maze], delay) if visualize else None

    while current != start:
        current.highlight()
        render_frame([maze], delay) if visualize else None

        neighbors = maze.navigable_neighbors(current)

        current = min(neighbors, key=lambda n: distances[n])

    current.highlight()
    render_frame([maze], delay) if visualize else None

    return maze

def a_star(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:

    # Helper function to calculate heuristic of current cell
    # h_score - distance from goal cell
    def heuristic(cell: Cell, goal: Cell) -> int:
        return abs(cell.row - goal.row) + abs(cell.col - goal.col)

    if current is None:
        current = maze.get_cell(0, 0)

    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)

    g_score = {cell: float("inf") for cell in maze.all_cells()} # distance from start
    f_score = {cell: float("inf") for cell in maze.all_cells()} # total score - f(n) = g(n) + h(n)
    came_from = {} # keep track of paths

    g_score[current] = 0
    f_score[current] = heuristic(current, goal)

    # Priority queue (f, cell)
    open_set = []
    heappush(open_set, (f_score[current], current.position, current)) # when f_scores are identical - checks start.position to not compare Cell types

    while open_set:
        _, _, current = heappop(open_set) # current min f_score

        if current.visited:  # Skip old entries
            continue
        current.visited = True
        render_frame([maze], delay) if visualize else None

        # Found goal
        if current == goal:
            # backtracking path from goal to start
            while current in came_from:
                current.highlight()
                render_frame([maze], delay) if visualize else None
                current = came_from[current]

            current.highlight()
            render_frame([maze], delay) if visualize else None

            return maze

        for neighbor in maze.navigable_neighbors(current):
            # Checks for new or better paths through neighbors
            # If neighbor wasn't visited - g_score[neighbor] = inf and tentative_g (distance of 1 from prev cell) is smaller
            # If neighbor was visited but through a more expensive path - tentative_g is smaller and overwrites the current path
            tentative_g = g_score[current] + 1  # all edges weight = 1
            if tentative_g < g_score[neighbor]:
                # Current path gets overwritten by the new cheaper path
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heappush(open_set, (f_score[neighbor], neighbor.position, neighbor))

    return maze
