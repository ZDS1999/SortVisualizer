from globals import SortWith
import globals
import time
from PySide2.QtCore import QThread, QObject, Signal

INFINITY = 0x40000


class SorterSignals(QObject):
    sig_compare = Signal(int)
    sig_time = Signal(float)
    sig_swap = Signal(int, int)
    sig_adjust = Signal(int, int)
    sig_sort_done = Signal(int)
    sig_change_button_status = Signal(int)


class Sorter(QThread):
    def __init__(self, sort_with, ms, amount, col_heights):
        super().__init__()
        self.sort_with = sort_with
        self.sort_delay = ms
        self.sort_done_delay = 2 if amount > 300 else 5
        self.amount = amount
        self.cols = col_heights
        self.signals = SorterSignals()
        self.comparisons = 0

    def run(self):
        start_time = time.time()
        if self.sort_with == SortWith.BUBBLE.value:
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
            print('should never come here: algorithm not exists')
        end_time = time.time()
        self.signals.sig_time.emit(end_time - start_time)
        if globals.RET_FLAG == False:
            self.sorted()

    # FUCTIONS THAT SEND SINGALS

    def sorted(self):
        for index in range(self.amount):
            self.signals.sig_sort_done.emit(index)
            self.msleep(self.sort_done_delay)
        self.signals.sig_change_button_status.emit(2)

    def swap(self, left, right):
        self.cols[left], self.cols[right] = self.cols[right], self.cols[left]
        self.signals.sig_swap.emit(left, right)

    def adjust(self, pos, height):
        self.signals.sig_adjust.emit(pos, height)

    def add_comparisons(self, addition):
        self.comparisons += addition
        self.signals.sig_compare.emit(self.comparisons)

    # SORT FUNCTIONS

    def bubble_sort(self):
        for i in range(self.amount):
            for j in range(self.amount - 1 - i):
                if globals.RET_FLAG == True:
                    return
                self.add_comparisons(1)
                if self.cols[j] > self.cols[j+1]:
                    self.swap(j, j+1)
                self.msleep(self.sort_delay)

    def select_sort(self):
        '''
            LHS     RHS
           sorted  unsorted
        find the minimun num in rhs and swap it to the next lhs location
        '''
        for i in range(self.amount):
            min_val = INFINITY
            min_pos = i
            for j in range(i, self.amount):
                if globals.RET_FLAG == True:
                    return
                self.add_comparisons(1)
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
                if globals.RET_FLAG == True:
                    return
                self.add_comparisons(1)
                self.cols[j] = self.cols[j-1]
                self.adjust(j, self.cols[j-1])
                self.msleep(self.sort_delay)
                j -= 1
            self.cols[j] = temp
            self.adjust(j, temp)
            self.msleep(self.sort_delay)

    def shell_sort(self):
        gap = self.amount // 2
        while gap > 0:
            for i in range(gap, self.amount):
                temp = self.cols[i]
                j = i
                while j >= 0 and j - gap >= 0 and temp < self.cols[j-gap]:
                    if globals.RET_FLAG == True:
                        return
                    self.add_comparisons(1)
                    self.cols[j] = self.cols[j-gap]
                    self.adjust(j, self.cols[j-gap])
                    self.msleep(self.sort_delay)
                    j -= gap
                self.cols[j] = temp
                self.adjust(j, temp)
                self.msleep(self.sort_delay)
            gap = gap // 2

    def merge_sort(self):
        def merge(reg, nums, start, end):
            if start >= end:
                return
            if globals.RET_FLAG == True:
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
                self.add_comparisons(1)
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
                if globals.RET_FLAG == True:
                    return
                nums[k] = reg[k]
                self.adjust(k, reg[k])
                self.msleep(self.sort_delay)

        reg = [0 for i in range(self.amount)]
        merge(reg, self.cols, 0, self.amount-1)
            
    def quick_sort(self):
        def sort(nums, start, end):
            if start >= end:
                return
            if globals.RET_FLAG == True:
                return
            l = start
            r = end
            temp = nums[l]
            while l < r:
                while l < r and nums[r] >= temp:
                    self.add_comparisons(1)
                    r -= 1
                if l < r:
                    # self.swap(l, r)
                    self.cols[l] = self.cols[r]
                    self.adjust(l, self.cols[r])
                    self.msleep(self.sort_delay)
                    l += 1
                while l < r and nums[l] <= temp:
                    self.add_comparisons(1)
                    l += 1
                if l < r:
                    # self.swap(l, r)
                    self.cols[r] = self.cols[l]
                    self.adjust(r, self.cols[l])
                    self.msleep(self.sort_delay)
                    r -= 1
            pivot = l
            self.cols[pivot] = temp
            self.adjust(pivot, temp)
            sort(nums, start, pivot-1)
            sort(nums, pivot+1, end)

        sort(self.cols, 0, self.amount-1)


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
                self.add_comparisons(1)
                cmax = ri
            # if parent and child node should be exchanged, then continue to heapify
            if self.cols[cmax] > self.cols[index]:
                self.add_comparisons(1)
                self.swap(cmax, index)
                self.msleep(self.sort_delay)
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
            if globals.RET_FLAG == True:
                return
            self.swap(0, i)
            self.msleep(self.sort_delay)
            max_heapify(0, i-1)


# test alogrithm's correctness
if __name__ == '__main__':
    import random
    from copy import deepcopy
    nums = []
    amount = 10
    for i in range(amount):
        nums.append(random.randint(1, 100))
    sorter = Sorter(0, 0, amount, nums)
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
