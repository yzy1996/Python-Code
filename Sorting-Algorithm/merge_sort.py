# merge_sort 归并排序

import time


def merge_sort(array):
    merge_out(array, 0, len(array) - 1)


def merge_out(array, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_out(array, low, mid)
        merge_out(array, mid + 1, high)
        merge_in(array, low, mid, high)


def merge_in(array, low, mid, high):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    # 将超出索引未添加进tmp的添加进去
    if i <= mid:  # 如果mid右边已添加，则需补充mid左边部分
        start, end = i, mid
    else:
        start, end = j, high
    tmp.extend(array[start:end + 1])  # 常规+1
    array[low:high + 1] = tmp


if __name__ == '__main__':
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    start = time.clock()
    merge_sort(array)
    print(array)
    end = time.clock()
    print('用时：', str(end - start))