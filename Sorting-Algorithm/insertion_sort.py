# insertion_sort 插入排序
# 取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。重复这个过程，直到未排序区间中元素为空，算法结束。

import time


def insertion_sort(array):
    length = len(array)
    if length <= 1:
        return

# 比较一下以下两种方法

    # for i in range(length - 1):
    #     while i >= 0 and array[i] > array[i + 1]:
    #         array[i + 1], array[i] = array[i], array[i + 1]
    #         i -= 1

    for i in range(1, length):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    start = time.clock()
    insertion_sort(array)
    print(array)
    end = time.clock()
    print('用时：', str(end - start))
