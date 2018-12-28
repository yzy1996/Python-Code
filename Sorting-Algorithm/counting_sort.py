# counting_sort 计数排序

import time


def counting_sort(array):
    if len(array) <= 1:
        return

    counts = [0] * (max(array) + 1)
    for num in array:
        counts[num] += 1

    # 临时数组，储存排序之后的结果
    array_sorted = []
    for i in range(max(array) + 1):
        array_sorted += [i] * counts[i]
    array[:] = array_sorted


if __name__ == '__main__':
    array = [5, 6, 1, 4, 2, 8, 10, 7, 6]
    start = time.clock()
    counting_sort(array)
    print(array)
    end = time.clock()
    print('用时：', str(end - start))