# -*- coding: utf-8 -*-
# @Author: [Your Name]
# @Date:   [Today's Date]
# @Email:  [Your Email]
# @Last Modified by:   [Your Name]
# @Last Modified time: [Today's Date]

# coding: utf-8
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))




