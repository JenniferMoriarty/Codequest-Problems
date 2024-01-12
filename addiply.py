import sys
import math
import string

cases = int(input().rstrip()) #this grabs the first number (how many lines)

for caseNum in range(cases):
    line = input().split()#read in all the input lines after the first
    for i in range(0, len(line)-1):
        print(int(line[i])+int(line[i+1]), int(line[i])*int(line[i+1]))
        