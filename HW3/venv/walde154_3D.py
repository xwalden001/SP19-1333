def stockStat(file,year):
    workingfile = open(file,'r')
    counter = 0
    summ = 0
    mean = 0
    for line in workingfile:
        lineidx = []
        line = line.split(',')
        lineidx = line[0][:4]
        if str(year) == lineidx:
            summ += float(line[4])
            counter +=1
    mean = round(summ/counter,2)
    file = file.replace('.csv','')
    workingfile.close()

    return 'The average closing value of '+ file + ' in '+ str(year)+ ' was $'+str(round(mean,2))

def maxGain(file):
    day = []
    month = []
    year = []
    gain = []
    realyr = ''
    check = ''
    checkday = ''
    months = {'01': 'January ','02': 'Feburary', '03':'March', '04': 'April','05':'May', '06': 'June', '07':'July', '08':'August', '09': 'September', '10': 'October','11':'November','12':'December'}
    workingfile = open(file,'r')
    for line in workingfile:
        line = line.split(',')
        year += line[0][:4]
        month += line[0][5:7]
        day += line[0][8:10]
        if line[0][0].isdigit() == True:
            gain.append(float(line[2]) - float(line[4]))
    idx = gain.index(max(gain))

    for ch in year[idx-1:idx+3]:
        realyr += ch
    for ch in month[idx-1:idx+1]:
        check += ch
    for ch in day[idx-1:idx+1]:
        checkday += ch
    day = checkday
    month = months[check]
    file = file.replace('.csv','')

    return 'The largest single day gain for '+file+' was '+ month+ ' '+day+', '+realyr+'.'
