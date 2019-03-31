import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
# explicitly set positions
pos = {0: (0, 0),
       1: (1, 0),
       2: (0, 1),
       3: (1, 1),
       4: (0.5, 2.0)}

# nx.draw_networkx_nodes(G, pos, node_color='r', node_size=20)
# nx.draw_networkx_edges(G, pos, edge_color='b', width=2)
# nx.draw_networkx_labels(G, pos, font_size=10)



G.add_edge('x','y')#添加边,起点为x，终点为y
# G.add_edges_from([(0,1),(1,3),(2,4)]) 
nx.draw(G, 
        with_labels=True, #这个选项让节点有名称
        edge_color='b', # b stands for blue! 
        # pos=pos, # 这个是选项选择点的排列方式，具体可以用 help(nx.drawing.layout) 查看
     # 主要有spring_layout  (default), random_layout, circle_layout, shell_layout   
     # 这里是环形排布，还有随机排列等其他方式  
        node_color='r', # r = red
        node_size=1000, # 节点大小
        width=3, # 边的宽度
       )
plt.axis('off')
plt.show()


# import matplotlib.pyplot as plt
# import networkx as nx

# G = nx.Graph()
# 把地图绘制出来
# def draw_map():
#     for i in range(len(road_label[0])):
#         G.add_edge(road_label[4][i],road_label[5][i])

#     nx.draw(G, 
#             with_labels=True, #这个选项让节点有名称
#             edge_color='b', # b stands for blue! 
#             # pos=pos,  
#             node_color='r', # r = red
#             node_size=1000, # 节点大小
#             width=3, # 边的宽度
#         )
#     print(nx.shortest_path(G, 35, 35))
    # nx.draw_networkx_edge_labels #  可以给路加上路名
    # plt.axis('off')
    # plt.show()
