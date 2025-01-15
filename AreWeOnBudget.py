cases = int(input())
for i in range(cases):
    num = int(input())
    line1 = input().split() #grab a line, put into list split by spaces
    line2 = input().split() #grab second line, put into second list
    line3 = [] #empty list to hold subtracted amounts
    for i in range(num):
        line3.append(float(line2[i])-float(line1[i])) #fill up 3rd list with subtracted values
    sum = 0
    for i in range(num):
        sum+=line3[i] #add em up

    print('%.2f'%(sum/num)) #find & print the average
