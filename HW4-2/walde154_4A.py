def digitSum(digit):
    if digit == 0:
        return digit
    else:
        return int(digit%10 + digitSum(digit/10))
