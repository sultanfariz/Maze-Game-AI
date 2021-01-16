import nodemodule as node
import numpy as np

def astar_search(maze, start, end):
    cost = 10
    start_node = node.Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    finish_node = node.Node(None, tuple(end))
    finish_node.g = finish_node.h = finish_node.f = 0

    yet_to_visit_list = []  
    visited_list = [] 
    
    yet_to_visit_list.append(start_node)
    
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 10

    move  =  [[-1, 0 ], # up
              [ 0, -1], # left
              [ 1, 0 ], # down
              [ 0, 1 ]] # right

    no_rows, no_columns = np.shape(maze)
    
    while yet_to_visit_list:
        outer_iterations += 1    
        
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        if outer_iterations > max_iterations:
            print ("melebihi batas maksimum iterasi")
            return node.return_path(current_node,maze)

        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)

        if current_node == finish_node:
            return node.return_path(current_node,maze)

        children = []

        for new_position in move: 

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if (node_position[0] > (no_rows - 1) or 
                node_position[0] < 0 or 
                node_position[1] > (no_columns -1) or 
                node_position[1] < 0):
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = node.Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            if ([visited_child for visited_child in visited_list if visited_child == child]):
                continue

            child.g = current_node.g + cost
            child.h = (((child.position[0] - finish_node.position[0]) ** 2) + 
                       ((child.position[1] - finish_node.position[1]) ** 2)) 
            child.f = child.g + child.h

            if ([x for x in yet_to_visit_list if child == x and x.g < child.g]) :
                continue
            yet_to_visit_list.append(child)