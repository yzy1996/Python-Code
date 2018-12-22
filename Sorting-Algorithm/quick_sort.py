# quick_sort 快速排序

import time
import random

def quick_sort(array):
    quick_out(array, 0, len(array) - 1)


def quick_out(array, low, high):
    if low < high:
        k = random.randint(low, high)
        array[low], array[k] = array[k], array[low] # 将分区点换到首位，避免了K的传参
        m = partition(array, low, high) 
        quick_out(array, low, m - 1)
        quick_out(array, m + 1, high)

# 返回pivot正确的位置索引（它的左边是比它小的，右边是比它大的）
def partition(array, low, high):
    pivot, j = array[low], low  # j指向pivot在的位置
    for i in range(low + 1, high + 1):  # i指向待比较元素的位置，从pivot后一位开始，因为pivot在首位
        if array[i] <= pivot:
            j += 1  # 此时j指向pivot应该在的位置
            array[j], array[i] = array[i], array[j]  # 先让待比较的元素交换位置
    array[low], array[j] = array[j], array[low]  # 真实交换pivot到它正确的位置
    return j



if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    start = time.clock()
    quick_sort(array)
    print(array)
    end = time.clock()
    print('用时：', str(end - start))