# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:24:50 2020

@author: carlb
"""

lines = open("Day2-input.txt", "r").read().split("\n")

def part1 ():
    # Count how many of the passwords have between a and b restricted letters
    validPasswords = 0
    for i in lines:
        if(i == ''): continue
        split = i.split(": ") # split[0] = restriction, split[1] = password
        rs = split[0].split(" ") # rs[0] = a-b, rs[1] = restricted letter
        restrictedLetter = rs[1]
        rangeSplit = rs[0].split("-")
        minimum = int(rangeSplit[0])
        maximum = int(rangeSplit[1])
        count = split[1].count(restrictedLetter)
        if(count >= minimum and count <= maximum):
            validPasswords += 1
    return validPasswords

def part2 ():
    # Count whether exacty one of the given indices is the given letter
    validPasswords = 0
    for i in lines:
        if(i == ''): continue
        split = i.split(": ") # split[0] = restriction, split[1] = password
        rs = split[0].split(" ") # rs[0] = a-b, rs[1] = restricted letter
        restrictedLetter = rs[1]
        rangeSplit = rs[0].split("-")
        idx1 = int(rangeSplit[0]) - 1
        idx2 = int(rangeSplit[1]) - 1
        if((split[1][idx1] == restrictedLetter) ^ (split[1][idx2] == restrictedLetter)):
            validPasswords += 1
    return validPasswords