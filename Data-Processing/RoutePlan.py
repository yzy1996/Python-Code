import classini
import math
import numpy

def read_input_file(path):
    with open(path) as f:
        label = []
        label = f.readline().strip('#\n()').split(',')  # 将第一行的标签提取出来
        lines = f.readlines()
        data = []                          
        for line in lines:              #把lines中的数据逐行读取出来
            temp = line.strip('\n()').split(',')  # 去掉字符串首尾以及中间的分隔符
            data.append(temp)
        data = [list(map(int, x)) for x in data]
        
        # 把每一列提取出来    
        for i in range(len(label)):  
            label[i] = [col_data[i] for col_data in data]

    return label


## 读取三种数据
###########################################################
# car(id,from,to,speed,planTime) 5_col
car_path = r'car.txt'
carfile=read_input_file(car_path)
car_list=[]
for i in range(len(carfile[0])):
    car_list.append(classini.Car(carfile[0][i],carfile[1][i],carfile[2][i],carfile[3][i],carfile[4][i]))

# road(id,length,speed,channel,from,to,isDuplex) 7_col
road_path = r'road.txt'
roadfile=read_input_file(road_path)
road_list=[]
for i in range(len(roadfile[0])):
    road_list.append(classini.road(roadfile[0][i],roadfile[1][i],roadfile[2][i],roadfile[3][i],roadfile[4][i],roadfile[5][i],roadfile[6][i]))

# cross(id,roadId,roadId,roadId,roadId) 5_col
cross_path = r'cross.txt'
crossfile=read_input_file(cross_path)
cross_list=[]
for i in range(len(crossfile[0])):
    cross_list.append(classini.Cross(crossfile[0][i],crossfile[1][i],crossfile[2][i],crossfile[3][i],crossfile[4][i]))

#############################################################
# 生成道路的邻接矩阵
def adjacency_matrix(list):
    n = len(list)
    Na = 1000
    output_matrix = [ [ Na for i in range(n) ] for j in range(n) ]

    for i in range(n):
        output_matrix[i][i] = 0
        output_matrix[list[i].begin_id][list[i].end_id] = list[i].length
        output_matrix[list[i].end_id][list[i].begin_id] = list[i].length

    return output_matrix

###############################################################
# 输入图G，返回其边与端点的列表
def getEdges(G):
    
    v1 = []     # 出发点
    v2 = []     # 对应的相邻到达点
    w  = []     # 顶点v1到顶点v2的边的权值
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] != 0:
                w.append(G[i][j])
                v1.append(i)
                v2.append(j)
    return v1,v2,w

def searchid(id):
    for i in range(len(cross_list)):
        if id == cross_list[i].ID:
            return i

#############################################################
# 寻找最短路径
def Bellman_Ford(start, INF=9999):
    # v1,v2,w = getEdges(G)
    # 初始化源点与所有点之间的最短距离
    dis = [INF for k in range(len(cross_list))]
    dis[searchid(start)] = 0
    path = [[] for k in range(len(cross_list))]
    path_id = [[] for k in range(len(cross_list))]
    # 核心算法
    for k in range(len(cross_list)-1):   
        check = 0           
        for i in range(len(road_list)):
            begin = searchid(road_list[i].begin_id) #0
            end = searchid(road_list[i].end_id) #1

            weight = road_list[i].length / ((numpy.log(road_list[i].path_number) + 1))

            if dis[begin] + weight < dis[end]:             
                dis[end] = dis[begin] + weight

                path[end] = []
                path[end] = path[begin]+path[end]
                path[end].append(road_list[i].begin_id)
                path[end].append(road_list[i].end_id)

                path_id[end] = []
                path_id[end] = path_id[begin]+path_id[end]
                path_id[end].append(road_list[i].ID)
               
                check = 1 

            elif road_list[i].isDuplex == 1 and dis[end] + weight < dis[begin]: 
                dis[begin] = dis[end] + weight

                path[begin] = []
                path[begin] = path[end]+path[begin]
                path[begin].append(road_list[i].end_id)
                path[begin].append(road_list[i].begin_id)   

                path_id[begin] = []           
                path_id[begin] = path_id[end]+path_id[begin]
                path_id[begin].append(road_list[i].ID)
             
                check = 1 
        if check == 0: 
            break
  
    return path_id

# 先全部生成所有的 [起点]->[终点]的路
pathlist = []

for i in range(len(cross_list)):  # 为每一个路起点生成最短的终点路径 
    pathlist.append(Bellman_Ford(cross_list[i].ID))

for i in range(len(car_list)):  # 为每辆车安排路线
    car_list[i].route = pathlist[searchid(car_list[i].begin_id)][searchid(car_list[i].end_id)]

# path = [[] for k in range(len(car_list))]
# for i in range(50):  
#     for p in car_list[i].route:
#         for j in range(len(road_list)):
#             if p == road_list[j].ID:
#                 car_list[i].routelen += road_list[j].length
#                 road_list[j].congestion += 1
#                 break

    # if i > 2000 - 1:
    #     for p in path[i - 2000]:
    #         for j in range(len(road_list)):
    #             if p == road_list[j].ID:
    #                 road_list[j].congestion -= 1
    #                 break
    # print(path[i])
###########################################################
# 3.ragular the realtime

N0=len(car_list)

car_list.sort(key=lambda x:x.maxspeed,reverse=True)#-+x.routelen/1000.0
#让快的先走

max_speed=[16,14,12,10,8,6,4,2]
N_in_a_time=[28,27,27,27,27,27,27,1]

timechange_point=0
timeflag=0
for i in range(len(car_list)):
    if car_list[i].maxspeed==max_speed[0]:
        if int(i/N_in_a_time[0])>timeflag:
            timeflag+=1
            timechange_point+=N_in_a_time[0]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)
        
    elif car_list[i].maxspeed==max_speed[1]:
        if int((i-timechange_point)/N_in_a_time[1])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[1]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)

    elif car_list[i].maxspeed==max_speed[2]:
        if int((i-timechange_point)/N_in_a_time[2])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[2]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)
    
    elif car_list[i].maxspeed==max_speed[3]:
        if int((i-timechange_point)/N_in_a_time[3])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[3]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)

    elif car_list[i].maxspeed==max_speed[4]:
        if int((i-timechange_point)/N_in_a_time[4])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[4]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)

    elif car_list[i].maxspeed==max_speed[5]:
        if int((i-timechange_point)/N_in_a_time[5])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[5]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)

    elif car_list[i].maxspeed==max_speed[6]:
        if int((i-timechange_point)/N_in_a_time[6])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[6]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)

    elif car_list[i].maxspeed==max_speed[7]:
        if int((i-timechange_point)/N_in_a_time[7])>0:
            timeflag+=1
            timechange_point+=N_in_a_time[7]
        car_list[i].realtime=car_list[i].planTime+int(timeflag)
#############################################################
with open('answer.txt', 'w') as f:
    for i in range(len(car_list)):   
        f.write('(')
        f.write(str(car_list[i].ID)+', ')

        ######################
        # 需要对出发时间进行规划
        f.write(str(car_list[i].realtime) + ', ')
        ######################

        f.write(str(car_list[i].route).strip('[]'))
        f.write(')')
        f.write('\n')
##########################################################