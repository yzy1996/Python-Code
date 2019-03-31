import math

def heuristic_distace(Neighbour_node,target_node):
    H = abs(Neighbour_node[0] - target_node[0]) + abs(Neighbour_node[1] - target_node[1])
    return H

def go_around(direction):
    box_length = 1
    diagonal_line = box_length * 1.4
    if (direction==0 or direction==2 or direction==6 or direction==8):
        return diagonal_line
    elif (direction==1 or direction==3 or direction==4 or direction==5 or direction==7):
        return diagonal_line

def find_coordinate(map,symble):
    #store coordinate
    result=[]
    for index1,value1 in enumerate(map):
        if symble in value1:
            row = index1
            for index2, value2 in enumerate(map[index1]):
                if symble==value2:
                   column = index2
                   result.append([row, column])
    return result

map =[[".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
      [".", ".", "#", ".", ".", "#", ".", "#", ".", "#"],
      ["s", ".", "#", ".", "#", ".", "#", ".", ".", "."],
      [".", "#", "#", ".", ".", ".", ".", ".", "#", "."],
      [".", ".", ".", ".", "#", "#", ".", ".", "#", "."],
      [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
      [".", "#", ".", ".", ".", "#", "#", ".", "#", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
      [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
      [".", ".", ".", "#", "#", "#", ".", ".", "#", "f"],
      ["#", "#", ".", ".", "#", "#", "#", ".", "#", "."],
      [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
      [".", ".", ".", ".", "#", "#", ".", ".", "#", "."]]

#these datas are store in the form of list in a singal list

obstacle = find_coordinate(map,"#")
start_node = find_coordinate(map,"s")[0]
target_node = find_coordinate(map,"f")[0]
current_node = start_node
path_vertices = [start_node]
#visited_vertices should be stored in the form of a singal list
Neighbour_vertices = []

while current_node != target_node:

    x_coordinate = current_node[0]
    y_coordinate = current_node[1]
    F = []
    Neighbour_vertices =   [[x_coordinate - 1, y_coordinate - 1],
                            [x_coordinate - 1, y_coordinate    ],
                            [x_coordinate - 1, y_coordinate + 1],
                            [x_coordinate,     y_coordinate - 1],
                            [x_coordinate    , y_coordinate    ],
                            [x_coordinate,     y_coordinate + 1],
                            [x_coordinate + 1, y_coordinate - 1],
                            [x_coordinate + 1, y_coordinate    ],
                            [x_coordinate + 1, y_coordinate + 1]]

    for index, value in enumerate(Neighbour_vertices):
        if value[0] in range(len(map)):
            if value[1] in range(len(map)):
               if value not in obstacle+path_vertices:
                    F.append(heuristic_distace(value, target_node) + go_around(index))
               else:
                    F.append(10000)
            else:
                    F.append(10000)
        else:
                    F.append(10000)
               #a very large number
    print(F)
    current_node=Neighbour_vertices[F.index(min(total_distance for total_distance in F))]
    print(current_node)

    path_vertices.append(current_node)
      # if current_node not in visited_vertices:
      #     visited_vertices.append(current_node)
      # else:
      #     print("there is no route between")
      #     break

print(path_vertices)
