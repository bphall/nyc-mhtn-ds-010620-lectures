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
        self.data = data

    @property
    def length(self):
        return len(self.data)

    @property
    def mean(self):
        return sum(self.data) / len(self.data)

    @property
    def stand_dev(self):
        sqrs = [((item - self.mean) ** 2) for item in self.data]
        return (sum(sqrs) / (len(self.data)-1)) ** .5

    @property
    def median(self):
        if len(self.data) % 2 == 0:
            return ((len(self.data) // 2) + ((len(self.data) // 2) + 1)) / 2
        else:
            return sorted(self.data)[(len(self.data) // 2)]

    def add_data(self, nums):
        self.data.extend(nums)

    def remove_data(self, nums):
        for i in nums:
            self.data.remove(i)

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




# CALCULATOR VERSION TWO WITHOUT PROPERTY DECORATORS

class Calculator:
    def __init__(self, data):
        self.data = data
        self.mean = self.get_mean()
        self.length = self.get_length()
        self.stand_dev = self.get_stand_dev()
        self.median = self.get_median()

    # @property
    def get_length(self):
        return len(self.data)

    # @property
    def get_mean(self):
        self.mean = sum(self.data) / len(self.data)
        return self.mean

    # @property
    def get_stand_dev(self):
        sqrs = [((item - self.mean) ** 2) for item in self.data]
        return (sum(sqrs) / (len(self.data)-1)) ** .5

    # @property
    def get_median(self):
        if len(self.data) % 2 == 0:
            return ((len(self.data) // 2) + ((len(self.data) // 2) + 1)) / 2
        else:
            return sorted(self.data)[(len(self.data) // 2)]

    def add_data(self, nums):
        self.data.extend(nums)
        self.mean = self.get_mean()
        self.length = self.get_length()

    def remove_data(self, nums):
        for i in nums:
            self.data.remove(i)
            self.mean = self.get_mean()
            self.length = self.get_length()