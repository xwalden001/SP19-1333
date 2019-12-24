def fileCleanup(strfile):
    for ch in strfile:
        if ch in '.,!();`:"':
            strfile = strfile.replace(ch,'')
    strfile = strfile.lower()
    return strfile




def topngram(file,gram):
    commonwords = ['of','the','i','he','she','a','it','is','was','be','not','my','    ','']
    grams = {}
    workinggram = ''
    workingfile = open(file,'r')
    for line in workingfile:
        line = fileCleanup(line)
        line = line.split(' ')
        for value in line:
           workinggram = ''
           if value not in commonwords:
                for i in range(0,gram,1):
                    if line[line.index(value)+i] == line[-1]:
                        break
                    else:
                        workinggram += ' '+ line[line.index(value)+i]

                if workinggram in grams:
                   grams[workinggram] += 1
                else:
                   grams[workinggram] = 1
    idx = max(grams.values())
    work = list(grams.values()).index(idx)
    answer = list(grams.keys())[work]
    print(answer)



