def tax(income):
    level1tax = 952.50#round((9525 *.1),2)
    level2tax = 3501.00#level1tax + round((29175*.12),2)
    level3tax = 9636.00#level1tax + level2tax + round((43800*.22),2)
    level4tax = 13600.00
    level5tax = 105000.00
    if income <= 9525:
        tax = round((income * .1),3)
        return tax

    if income > 9525 and income <= 39700:
        taxedincome = (income - 9525)*.12
        tax = round((taxedincome),2)+(level1tax)
        return tax

    if income > 38700 and income <= 82500:
        tax = round(((income-38700) * .22),2)+(level1tax)+(level2tax)
        return tax

    if income > 82500 and income <= 157500:
        tax = (level1tax)+(level2tax)+(level3tax)+round((income-82500 * .24),2)
        return tax

    if income > 157500 and income <= 200000:
        tax = level1tax + level2tax + level3tax + round((income-157500 * .32),2)
        return tax

    if income > 200000 and income <= 500000:
        tax = level1tax + level2tax + level3tax + level4tax +round((income-200000 * .35),2)
        return tax

    if income > 500000:
        tax = level1tax + level2tax + level3tax + level4tax + level5tax+round((income-500000 * .37),2)
        return tax
