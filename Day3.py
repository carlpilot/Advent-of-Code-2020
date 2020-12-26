# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:46:12 2020

@author: carlb
"""

lines = open("Day3-input.txt", "r").read().split("\n")

def part1 (r = 3, d = 1):
    # How many trees (#) will be hit travelling right 3, down 1?
    x = 0
    y = 0
    treesHit = 0
    for i in lines:
        if(isTree(x, y)):
            treesHit += 1
        x += r
        y += d
    return treesHit
    
def isTree (x, y):
    if(y >= len(lines) or len(lines[y]) == 0): return False
    return lines[y][x % len(lines[y])] == "#"
    
def part2 ():
    return part1(r=1) * part1() * part1(r=5) * part1(r=7) * part1 (r=1, d=2)