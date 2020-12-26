# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:57:30 2020

@author: carlb
"""

import re

requiredCredentials = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part1 ():
    # Count how many passports have all the required parameters except CID
    passports = open("Day4-input.txt", "r").read().split("\n\n")
    validPassports = 0
    for i in passports:
        containsAll = True
        for j in requiredCredentials:
            if(not j in i):
                containsAll = False
                break
        if(containsAll):
            validPassports += 1
    return validPassports

def part2 ():
    # More strictly validate passports
    passports = open("Day4-input.txt", "r").read().split("\n\n")
    validPassports = 0
    idx = 0
    for i in passports:
        idx += 1
        byr = re.search("byr:19[2-9][0-9]|byr:200[0-2]( |\n|\Z)", i) != None
        iyr = re.search("(iyr:201[0-9]|iyr:2020)( |\n|\Z)", i) != None
        eyr = re.search("(eyr:202[0-9]|eyr:2030)( |\n|\Z)", i) != None
        hgtCM = re.search("(hgt:1[5-8][0-9]cm|hgt:19[0-3]cm)( |\n|\Z)", i) != None
        hgtIN = re.search("(hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in)( |\n|\Z)", i) != None
        hgt = hgtCM or hgtIN
        hcl = re.search("(hcl:#[0-9a-f]{6})( |\n|\Z)", i) != None
        ecl = re.search("(ecl:(amb|blu|brn|gry|grn|hzl|oth))( |\n|\Z)", i) != None
        pid = re.search("pid:[0-9]{9}( |\n|\Z)", i) != None
        if(byr and iyr and eyr and hgt and hcl and ecl and pid):
            validPassports += 1
            print("---")
            print(i)
            print("byr  iyr  eyr  hgt  hcl  ecl  pid")
            print(byr, iyr, eyr, hgt, hcl, ecl, pid) 
        if(idx == 3):
            print(i)
            print("byr  iyr  eyr  hgt  hcl  ecl  pid")
            print(byr, iyr, eyr, hgt, hcl, ecl, pid) 
    return validPassports
        
    