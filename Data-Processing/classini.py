class Car(object):
    def __init__(self, ID, begin_id, end_id,maxspeed,planTime):
        self.ID = ID
        self.begin_id=begin_id
        self.end_id=end_id
        self.maxspeed = maxspeed
        self.planTime=planTime
        self.realtime=self.planTime
        self.state=0
        self.routelen=0   # 路径总长度
        #state: 
        # 0:未出车
        # 1:等待状态(没有到达终点)
        # 2:终止状态(没有到达终点)
        # 3:已到达
        self.route=[]
        self.position=0
        self.roadID=0
        self.path=0
        self.pathdir='no'
        #pathdir: 
        # no:未出车或已到达
        # go
        # back



class Cross(object):
    def __init__(self,ID,roadId1,roadId2,roadId3,roadId4):
        self.ID=ID
        self.roadId1 = roadId1
        self.roadId2 = roadId2
        self.roadId3 = roadId3
        self.roadId4 = roadId4
        self.roadlist=sorted([self.roadId1,self.roadId2,self.roadId3,self.roadId4])

class road(object):
    def __init__(self, ID, length, maxspeed,path_number,begin_id,end_id,isDuplex):
        self.ID = ID
        self.length = length
        self.maxspeed = maxspeed
        self.path_number=path_number
        self.begin_id=begin_id
        self.end_id=end_id
        self.isDuplex=isDuplex
        self.situation=[] #此道路里面的车辆的情况
        self.congestion=0 #道路拥堵情况，即该路上安排了几辆车