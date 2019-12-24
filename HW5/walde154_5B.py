def markup2HTML(file):
    workingfile = open(file,'r')
    htmlfile = open(file[:file.find('.')] + '.html','w')
    file = file[:file.find('.')] + '.html'
    htmlfile.write('<html><head> <title> CSCI1133 Markup </title> </head><body>')
    for line in workingfile:
        line = line.replace('/','^')
        if '\n' in line:
            line = line.replace('\n','<br/>')
        if '*' in line:
            idx = 0
            line = line.replace('*','</b>')
            idx = line.find('</b>')
            line = line[:idx]+'<b>'+line[idx+4:]
        if '_' in line:
            idx = 0
            line = line.replace('_','</u>')
            idx = line.find('</u>')
            line = line[:idx] + '<u>' + line[idx + 4:]
        if '--' in line:
            idx = 0
            line = line.replace('--', '</strike>')
            idx = line.find('</strike>')
            line = line[:idx] + '<strike>' + line[idx + 9:]
        if '^' in line:
            idx = 0
            line = line.replace('^','</i>')
            idx = line.find('</i>')
            line = line[:idx] + '<i>' + line[idx + 4:]
        if '#' in line:
            line = line.replace('#',"</span>")
            idx = line.find("</span>")
            line = line[:idx]+"<span style='color:#%s%s%s%s%s%s'>" %(line[idx+7],line[idx+8],line[idx+9],line[idx+10],line[idx+11],line[idx+12]) + line[idx+13:]


        htmlfile.write(line)
    htmlfile.write('</body></html>')
    workingfile.close()
    htmlfile.close()







markup2HTML('markup.txt')