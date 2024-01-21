nums = []
hours = 0
minutes = 0

cases = int(input().rstrip())
for i in range(cases):
    nums.clear()
    hours = 0
    minutes = 0
    line = input().rstrip().split(",")
    #print(line)
    for j in range(len(line)-1):
        nums.append((line[j+1]).split(":"))
    #print(nums)
    for k in range(len(nums)):
        hours += int(nums[k][0])
        minutes += int(nums[k][1])
        hours += int(minutes/60)
        minutes = minutes%60 #strip the hours off
        
    if hours >= 1 and hours<2:
        HourWord = "hour"
    else:
        HourWord = "hours"
        
    if minutes == 1:
        MinuteWord = "minute"
    else:
        MinuteWord = "minutes"
        
    if minutes == 0:
        print(line[0] + "=" + str(hours), HourWord)
    else:
        print(line[0] + "=" + str(hours), HourWord, minutes, MinuteWord)
        
    
