# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:14:25 2020

@author: carlb
"""

expenses = open("Day1-input.txt", "r").read().split("\n")
expenses = expenses[0:len(expenses)-2] # remove last blank value

def part1 ():
    # 2 numbers sum to 2020. What is their product?
    for i in expenses:
        for j in expenses:
            if(int(i) + int(j) == 2020):
                return int(i) * int(j)
    print("No matches")

def part2 ():
    # 3 numbers sum to 2020. What is their product?
    for i in expenses:
        for j in expenses:
            for k in expenses:
                if(int(i) + int(j) + int(k) == 2020):
                    return int(i) * int(j) * int(k)
    print("No matches")