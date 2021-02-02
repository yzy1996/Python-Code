# Bubble Sort 冒泡排序
# 冒泡排序只会操作相邻的两个数据。每次冒泡操作都会对相邻的两个元素进行比较，交换为正确的顺序，重复N次，时间复杂度为O(n^2)
# 优化的地方在于：当某次排序已经没有数据可以交换，就可以停止了
import time


def bubble_sort(array):
    length = len(array)
    if length <= 1:
        return

    for i in range(length):
        made_swap = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                made_swap = True
        if not made_swap:
            break


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    start = time.clock()
    bubble_sort(array)
    print(array)
    end = time.clock()
    print('用时：', str(end - start))
