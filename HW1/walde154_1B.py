def makeChange(change):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    if change//.25 != 0:
        quarters = change//.25
        change = round((change - (quarters*.25)),2)
    if change//.10 != 0:
        dimes = change//.10
        change = round((change - (dimes*.10)),2)
    if change//.05 != 0:
        nickels = change//.05
        change = round((change - (nickels *.05)),2)
    if change//.01 != 0:
        pennies = round((change/.01),2)
    return "Quarters: "+str(int(quarters))+", Dimes: "+str(int(dimes))+", Nickels: "+str(int(nickels))+", Pennies: "+str(int(pennies))
