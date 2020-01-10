#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math
from typing import List

import numpy




class Calculator:
    def __init__(self, data):
        self._data = data

    @property
    def length(self):
        return len(self._data)

    @property
    def mean(self):
        return sum(self._data) / len(self._data)

    @property
    def stand_dev(self):
        sqrs = [((item - self.mean) ** 2) for item in self._data]
        return (sum(sqrs) / (len(self._data) - 1)) ** .5

    @property
    def median(self):
        if len(self._data) % 2 == 0:
            return ((len(self._data) // 2) + ((len(self._data) // 2) + 1)) / 2
        else:
            return sorted(self._data)[(len(self._data) // 2)]

    def add_data(self, nums):
        self._data.extend(nums)

    def remove_data(self, nums):
        for i in nums:
            self._data.remove(i)

    # @property
    # def stand_dev(self):
    #     sqrs = [((item - self.mean) ** 2) for item in self.data]
    #     return (sum(sqrs))**.5


# class BadCalculator:
#     def __init__(self, data):
#         self._data = data
#         self.mean = sum(data)/len(data)
#
#     def add_data(self, xs):
#         self._data.extend(xs)
#         self.mean = sum(self._data) / len(self._data)


# if __name__ == '__main__':
#     bc = BadCalculator([1, 3, 8])
#     print(f'old mean: {bc.mean}')
#     bc.add_data([2, 1])
#     print(f'new mean: {bc.mean}')
#     print(f'correct new mean: {sum(bc._data) / len(bc._data)}')
#
#     bc._data.append(10)
#     print(f'new new mean: {bc.mean}')
#     print(f'correct new new mean: {sum(bc._data) / len(bc._data)}')
