# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:14:25 2020

@author: carlb
"""

expenses = open("Day1-input.txt", "r").read().split("\n")
expenses = expenses[0:len(expenses)-2] # remove last blank value

def run ():
    for i in expenses:
        for j in expenses:
            if(int(i) + int(j) == 2020):
                print(int(i) * int(j))
                return
    print("No matches")

run()