from datetime import datetime , date
import dates

today = date.today()

d4 = today.strftime("%B %d")


day = dates.days



def getmsginfo(dayinfo):
    date = dayinfo[0] + ' ' + dayinfo[1]

    morning = dayinfo[2]
    afternoon = dayinfo[3]
    afternoon = list(afternoon)
    afternoon[0] = str(int(afternoon[0]) + 12)
    afternoon = ''.join(afternoon)


    return [morning, afternoon, dayinfo[3]] 



def getcurrentday():
    for i in range(len(day)):
        if d4 == day[i][0]:
            today = day[i]
            times = getmsginfo(today)
        else:
            pass
    return times



def calc():
    times = getcurrentday()
    morning = datetime.strptime(times[0],'%H:%M')
    afternoon = datetime.strptime(times[1],'%H:%M')
    currenttime  = datetime.today()
    current = currenttime.strftime('%H:%M')
    current = datetime.strptime(current, '%H:%M')
    morningcount = morning - current
    afternooncount = afternoon - current
    
    return [morningcount, afternooncount, times[2], times[0]]

