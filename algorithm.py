from globals import SortWith
from PySide2.QtCore import QThread, QObject

INFINITY = 0x40000

class Sorter(QThread):
    def __init__(self, sort_with, ms, amount, col_heights):
        super().__init__()
        self.sort_with  = sort_with
        self.sort_delay = ms
        self.amount     = amount
        self.cols       = col_heights

    def run(self):
        print('...')
        if self.sort_with   == SortWith.BUBBLE.value:
            self.bubble_sort()
        elif self.sort_with == SortWith.SELECT.value:
            self.select_sort()
        elif self.sort_with == SortWith.INSERT.value:
            self.insert_sort()
        elif self.sort_with == SortWith.SHELL.value:
            self.shell_sort()
        elif self.sort_with == SortWith.MERGE.value:
            self.merge_sort()
        elif self.sort_with == SortWith.QUICK.value:
            self.quick_sort()
        elif self.sort_with == SortWith.HEAP.value:
            self.heap_sort()
        else:
            print('should never come here: alogrithm not exists')

    def swap(self, i, j):
        self.cols[i], self.cols[j] = self.cols[j], self.cols[i]

    def bubble_sort(self):
        for i in range(self.amount):
            for j in range(self.amount - 1 - i):
                if self.cols[j] > self.cols[j+1]:
                    self.swap(j, j+1)
                self.msleep(self.sort_delay)

    def select_sort(self):
        for i in range(self.amount):
            min_val = INFINITY
            min_pos = i
            for j in range(i, self.amount):
                if self.cols[j] < min_val:
                    min_val = self.cols[j]
                    min_pos = j
                self.msleep(self.sort_delay)
            self.swap(i, min_pos)

    def insert_sort(self):
        for i in range(1, self.amount):
            temp = self.cols[i]
            j = i
            while j >= 0 and j - 1 >= 0 and temp < self.cols[j-1]:
                self.cols[j] = self.cols[j-1]
                j -= 1
            self.cols[j] = temp

    def shell_sort(self):
        gap = self.amount // 2
        while gap > 0:
            for i in range(gap, self.amount):
                temp = self.cols[i]
                j = i
                while j >= 0 and j - gap >= 0 and temp < self.cols[j-gap]:
                    self.cols[j] = self.cols[j-gap]
                    j -= gap
                self.cols[j] = temp
            gap = gap // 2

    def merge_sort(self):
        def merge(reg, nums, start, end):
            if start >= end:
                return
            mid = (start + end) // 2
            start1 = start
            end1 = mid
            start2 = mid + 1
            end2 = end
            merge(reg, nums, start1, end1)
            merge(reg, nums, start2, end2)
            k = start
            while start1 <= end1 and start2 <= end2:
                if nums[start1] < nums[start2]:
                    reg[k] = nums[start1]
                    k += 1
                    start1 += 1
                else:
                    reg[k] = nums[start2]
                    k += 1
                    start2 += 1
            while start1 <= end1:
                reg[k] = nums[start1]
                k += 1
                start1 += 1
            while start2 <= end2:
                reg[k] = nums[start2]
                k += 1
                start2 += 1
            for k in range(start, end+1):
                nums[k] = reg[k]

        reg = [0 for i in range(self.amount)]
        merge(reg, self.cols, 0, self.amount-1)
            
    def quick_sort(self):
        def partition(nums, start, end):
            l = start
            r = end
            while l < r:
                while l < r and nums[r] >= nums[l]:
                    r -= 1
                if l < r:
                    self.swap(l, r)
                    l += 1
                while l < r and nums[l] <= nums[r]:
                    l += 1
                if l < r:
                    self.swap(l, r)
                    r -= 1
            return l

        def quick(nums, start, end):
            if start >= end:
                return
            pivot = partition(nums, start, end)
            quick(nums, start, pivot-1)
            quick(nums, pivot+1, end)

        quick(self.cols, 0, self.amount-1)


    def heap_sort(self):
        def max_heapify(index, length):
            li = ( index << 1 ) + 1  # left child index
            ri = li + 1              # right child index
            cmax = li                # max child index: assume that camx is left
            # if index is child node
            if li > length:
                return
            # if right child < left child
            if ri <= length and self.cols[ri] > self.cols[li]:
                cmax = ri
            # if parent and child node should be exchanged, then continue to heapify
            if self.cols[cmax] > self.cols[index]:
                self.swap(cmax, index)
                max_heapify(cmax, length)

        '''
        FIRST STEP: HEAPITY THE ARRAY
        begin_index = the first non-child node
        child node can be regarded as heapified
        '''
        length = self.amount - 1
        begin_index = ( length >> 1 ) -1
        for i in range(begin_index, -1, -1):
            max_heapify(i, length)
        '''
        SECOND STEP: SORT THE MAX HEAP
        repeat
            move the maximum number to the end of the array,
            reduce length by 1 and heapify the array
        for length-1 times
        '''
        for i in range(length, 0, -1):
            self.swap(0, i)
            max_heapify(0, i-1)


# test alogrithm's correctness
if __name__ == '__main__':
    import random
    from copy import deepcopy
    nums = []
    for i in range(8):
        nums.append(random.randint(1, 100))
    sorter = Sorter(0, 0, 8, nums)
    # bubble_sort
    print('bubble_sort')
    print(nums)
    sorter.bubble_sort()
    print(nums, '\n')

    # select_sort
    random.shuffle(nums)
    print('select_sort')
    print(nums)
    sorter.select_sort()
    print(nums, '\n')

    # insert_sort
    random.shuffle(nums)
    print('insert_sort')
    print(nums)
    sorter.insert_sort()
    print(nums, '\n')

    # shell_sort
    random.shuffle(nums)
    print('shell_sort')
    print(nums)
    sorter.shell_sort()
    print(nums, '\n')

    # merge_sort
    random.shuffle(nums)
    print('merge_sort')
    print(nums)
    sorter.merge_sort()
    print(nums, '\n')

    # quick_sort
    random.shuffle(nums)
    print('quick_sort')
    print(nums)
    sorter.quick_sort()
    print(nums, '\n')

    # heap_sort
    random.shuffle(nums)
    print('heap_sort')
    print(nums)
    sorter.heap_sort()
    print(nums, '\n')
