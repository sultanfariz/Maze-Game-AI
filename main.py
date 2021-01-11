import numpy as np
import astarmodule as astar
import greedymodule as greedy
import nodemodule as node


if __name__ == '__main__':  

    maze = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]  
    
    start = [0, 1]; end = [11,15]; cost = 20
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 0

    # print(path)
    path_astar = astar.astar_search(maze,cost, start, end)
    path_greedy = greedy.greedy_search(maze,cost, start, end)
    print('\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in maze]))
    print('\n')
    print('\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path_astar]))
    print('\n')
    print('\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path_greedy]))
    print('\n')