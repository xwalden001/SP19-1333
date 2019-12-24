def igpay(phrase):
    flag = False
    up = False
    new = ''
    vowels = "aeiou"
    uppers = ''
    #if '?' in phrase:
    #    flag = True
    #    phrase = phrase.replace('?','')
    if phrase[0] == phrase[0].upper():
        up = True
    phrase = phrase.lower()
    phrase = phrase.split(' ')
    for value in phrase:
        print(value)
        for i in value:
            punct = ''
            if i in ',.?;:!':
                punct += i
                value = value.replace(i ,'')
        for ch in value:
            #punct = ''
            #if ch == 'y':
            #    new += value[value.find(ch)+1:] + 'yay '
            #    break

            if ch in vowels and ch == value[0]:
                new += str(value) + 'way'
                break
            if ch in vowels:
                new += value[value.find(ch):] + value[:value.find(ch)] + 'ay'
                break
        if phrase[-1] == value:
            new+=''
        else:
            new += ''

        new += punct + ' '
    if up == True:
        new = new[0].upper()+ new[1:]



    return new.strip()

