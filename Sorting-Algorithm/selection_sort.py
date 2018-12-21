# selection_sort 选择排序
# 选择排序算法的实现思路有点类似插入排序，也分已排序区间和未排序区间。但是选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。

import time


def insertion_sort(array):
    length = len(array)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_val = array[i]
        for j in range(i, length):
            if array[j] < min_val:
                min_val = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    start = time.clock()
    insertion_sort(array)
    print(array)
    end = time.clock()
    print('用时：', str(end - start))