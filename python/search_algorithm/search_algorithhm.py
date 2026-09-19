
# Manhattan Distance Heuristic Search Algorithm
# =============================================

# Instead of looking blindly in all directions, the Manhattan Distance heuristic function
# calculates the sum of the absolute differences between the coordinates of two points on
# a grid to work out the shortest path. Also known as the A* method.

# Designed by Surjit Randhawa 2026


import heapq

class Node:
    # Represents a coordinate in the grid with path-finding costs.
    def __init__(self, position, parent=None):
        self.position = position  # (x, y) tuple
        self.parent = parent      # Keeps track of the path trail
        
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic: Estimated cost from current node to end
        self.f = 0  # Total cost (f = g + h)
        
    def __lt__(self, other):
        # Tie-breaker for the priority queue (heapq)
        return self.f < other.f

def manhattan_distance(p1, p2):
    #Heuristic function estimating the remaining distance using grid movement.
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star_routine(grid, start, end):
    # Finds the shortest path on a 2D grid from start to end avoiding obstacles.
    # 0 = Empty space, 1 = Obstacle/Wall
    
    grid_height = len(grid)
    grid_width = len(grid[0])
    
    # Initialize start and end nodes
    start_node = Node(start)
    end_node = Node(end)
    
    # open_list stores nodes to be evaluated (tracked as a min-heap priority queue)
    open_list = []
    # closed_set stores positions already evaluated for performance
    closed_set = set()
    
    # Push the start node onto the open list
    heapq.heappush(open_list, start_node)
    
    # Map to track the best g-score (cost) found so far for any position
    best_g = {start: 0}
    
    # Movement vectors: Up, Down, Left, Right (4-way movement)
    movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    while open_list:
        # Get the node with the lowest total cost 'f'
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position
        
        # If we reached the goal, reconstruct and return the path
        if current_pos == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path (start to end)
            
        closed_set.add(current_pos)
        
        # Explore neighbours
        for move in movements:
            neighbour_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            
            # 1. Check grid boundaries
            if not (0 <= neighbour_pos[0] < grid_width and 0 <= neighbour_pos[1] < grid_height):
                continue
                
            # 2. Check if walkable (0 is open, 1 is a wall)
            if grid[neighbour_pos[1]][neighbour_pos[0]] == 1:
                continue
                
            # 3. Skip if already fully evaluated
            if neighbour_pos in closed_set:
                continue
                
            # Calculate tentative g-score (moving 1 step costs 1 unit)
            tentative_g = current_node.g + 1
            
            # 4. If this path to neighbour is worse than a previously found one, skip it
            if neighbour_pos in best_g and tentative_g >= best_g[neighbour_pos]:
                continue
                
            # Create the valid neighbour node
            neighbour_node = Node(neighbour_pos, current_node)
            neighbour_node.g = tentative_g
            neighbour_node.h = manhattan_distance(neighbour_pos, end_node.position)
            neighbour_node.f = neighbour_node.g + neighbour_node.h
            
            # Record this as the best known path to this neighbour position
            best_g[neighbour_pos] = tentative_g
            heapq.heappush(open_list, neighbour_node)
            
    return None # Return None if no path exists


# Demonstration
if __name__ == "__main__":
    # Define a 7x7 grid. 0 is open space, 1 is an impassable wall.
    # We will build a wall cutting straight through the middle.
    maze = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]
    ]
    
    start_point = (0, 0) # Top-left corner
    end_point = (6, 6)   # Bottom-right corner
    
    shortest_path = a_star_routine(maze, start_point, end_point)
    
    print("Calculated Shortest Path:")
    print(shortest_path)
    
    # Display the grid path output
    if shortest_path:
        for y, row in enumerate(maze):
            row_str = ""
            for x, val in enumerate(row):
                if (x, y) == start_point:
                    row_str += " S "
                elif (x, y) == end_point:
                    row_str += " E "
                elif (x, y) in shortest_path:
                    row_str += " * " # Path taken
                elif val == 1:
                    row_str += " X " # Obstacle
                else:
                    row_str += " . " # Empty space
            print(row_str)

