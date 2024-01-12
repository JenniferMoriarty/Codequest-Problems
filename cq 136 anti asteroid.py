import sys
import math
import string

#get the first number (the number of lines to read)
cases = int(sys.stdin.readline().rstrip())

#use the variable on line 6 to read that many lines
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    data = line.split(" ")
    for i in range(len(data)):
        data[i] = int(data[i])
    print(data)
    num = math.sqrt((0-data[0])**2 + (0-data[1])**2)
    print( num)

    