def convertTime(time):
    index = time.find('m')
    f_hour = time.find(':')
    minutes = time[f_hour + 1] + time[f_hour + 2]

    if(f_hour > 1):
        hour = time[f_hour - 2] + time[f_hour - 1]

    else:
        hour = time[f_hour - 1]


    Day = time[index - 1] + time[index] 

    if(hour == '12' and Day == 'am'):
          hour = '00' 

    if(Day == 'pm'):
        hour = str(int(hour) + 12)
        
    if(int(hour) < 8):
        hour = '0' + hour


    print(f"{hour}:{minutes}")
    

    

