import time
import threading

# 你需要排序的序列（可以包含负数）
num = [-5, 3, 9, 11, -1, 3, 12, 0, 8, -3, 23, 5, 19]


# 睡眠的方法
def doSleep(func):
    co = 0.02  # 添加系数让睡眠时间短一些
    time.sleep(co * pow(1.1, float(func)))  # 使用幂函数就不怕负数排序了
    print(func)


# 将多个线程存在一个数组中
thread_list = []
for i in range(len(num)):
    temp = threading.Thread(target=doSleep, args=(str(num[i]), ))
    thread_list.append(temp)

if __name__ == '__main__':
    start = time.clock()
    for t in thread_list:
        t.start()  # 开启线程
    for t in thread_list:
        t.join()  # 所有子线程都结束了主线程才关闭
    end = time.clock()
    print('用时：', str(end - start))
