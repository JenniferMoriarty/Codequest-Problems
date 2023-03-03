import sys #helps with stuff like readline

cases = int(sys.stdin.readline().rstrip()) #holds a number
firstPart = []
secondPart = []

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip() #holds words
    firstPart.append(line+" =")
    #print(line, "=", end = " ") #print first part

    #split the line into two variables (split at the |)
    first, second  = (value for value in line.split("|"))
    first.rstrip() #get rid of any spaces
    second.rstrip()
    first = sorted(first) #puts stuff in order
    second = sorted(second)
    if first == second:
        secondPart.append("ANAGRAM")
    else:
        secondPart.append("NOT AN ANAGRAM")

for i in range (len(firstPart)):
    print(firstPart[i], secondPart[i])