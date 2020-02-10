#function of converting date times to timezone-aware date time
 
#Used pytz mitlicensed 
#Author Stuart Bishop <stuart@stuartbishop.net>
#https://pypi.org/project/pytz/
#Used tzlocal mitlicensed
#https://pypi.org/project/tzlocal/
#Maintainer Lennart Regebro, regebro@gmail.com



import datetime
import pytz #pip3 install pytz mitlicensed
import tzlocal #pip3 install tzlocal mitlicensed

dt = datetime.datetime(2019,8,21,16,36) #enter year, month, day, hour, minute, second, millisecond
#without the information of timezone dt remains timezone-unknown
#give a timezone information using pytz and datetime lib
timezone = (‘Asia/Seoul’) #I am currently in Seoul Korea. You can also call forth the local time using datetime.datetime.now()
#Also you can use tzlocal.get_localzone() to get your timezone information
dtaware = dt.astimezone(pytz.timezone(timezone))

#example
#dt = ~
#tz = (‘Asia/Seoul’)
def converttimeaware(dt,tz):
    dtaware = dt.astimezone(pytz.timezone(tz))
    return dtaware



# o Let Python figure out how to add 2 hours to 2018-12-31 23:18:03.

addtime = dtaware + datetime.timedelta(hours=2)

#example
#dtaware = ~
#tz = ~
#timechange = date time.timedelta(whatevertime=sometime)

def addtimefunction(dtaware,tz,timechange):
    addtime = dtaware + timechange
    return addtime #no need to set addtime; addtime is to show the method



# o Let Python figure out how to add 2 hours to 2018-03-11 01:45:00 (Daylight savings time
in 2018 started at 2AM on 2018-03-11).

daylightsavingtime = pytz.timezone(‘America/Chicago’).normalize(dtaware)
timezone = pytz.timezone(‘America/Chicago’)
def dst(dtaware,timezone)
    new time = timezone.normalize(dtaware)
    return newtime


__________________________________________________________________________________________

#let’s say the csv file is:

#datetime  timezone

#1         ‘1/1’
#2         ‘2/2’
#.
#.
#.


import csv

with open("test.csv", "r") as f:
    reader = csv.reader(f, delimiter=" ")
    total length = 0
    for i, line in enumerate(reader):
        'line[{}] = {}'.format(i, line)
        totallength +=1

for i in range(totallength):
    globals()[‘dt%s’ % i] = datatime.datatime(line[i][1])
    globals()[‘tz%s’ % i] = (line[i  ][2])


#use these dt and tz in the functions above


