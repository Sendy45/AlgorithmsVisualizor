from visualization import render_frame, Cell, Maze
from random import shuffle

def depth_first_search(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:

    if current is None:
        current = maze.get_cell(0, 0)

    current.visited = True
    render_frame([maze], delay) if visualize else None

    """if current == maze.get_cell(maze.rows - 1, maze.cols - 1):
        return maze # Goal found, stop recursion"""

    neighbors = maze.get_neighbors(current)
    shuffle(neighbors)

    for neighbor in neighbors:
        if not neighbor.visited:
            current.del_walls(neighbor)
            result = depth_first_search(maze, neighbor, visualize, delay)
            if result: # Stop exploring if goal was found
                return result


    return None