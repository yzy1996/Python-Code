import classini
import read
# 路径规划算法集合

# 生成邻接矩阵
# input数据类型：列表list
# output数据类型：列表List
def adjacency_matrix(list):
    n = len(list)
    Na = 1000
    output_matrix = [ [ Na for i in range(n) ] for j in range(n) ]

    for i in range(n):
        output_matrix[i][i] = 0
        output_matrix[list[i].begin_id][list[i].end_id] = list[i].length
        output_matrix[list[i].begin_id][list[i].end_id] = list[i].length

    return output_matrix



if __name__ == '__main__':
    car_path = r'car.txt'
    carfile=read.read_input_file(car_path)

    car_list=[]
    for i in range(len(carfile[0])):
        car_list.append(classini.Car(carfile[0][i],carfile[1][i],carfile[2][i],carfile[3][i],carfile[4][i]))

    road_path = r'road.txt'
    roadfile=read.read_input_file(road_path)

    road_list=[]
    for i in range(len(roadfile[0])):
        road_list.append(classini.road(roadfile[0][i],roadfile[1][i],roadfile[2][i],roadfile[3][i],roadfile[4][i],roadfile[5][i],roadfile[6][i]))

    cross_path = r'cross.txt'
    crossfile=read.read_input_file(cross_path)

    cross_list=[]
    for i in range(len(crossfile[0])):
        cross_list.append(classini.Cross(crossfile[0][i],crossfile[1][i],crossfile[2][i],crossfile[3][i],crossfile[4][i]))

    print(adjacency_matrix(road_list))