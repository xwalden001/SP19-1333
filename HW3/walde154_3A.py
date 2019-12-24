import math

def stdev(nums):
    standardDeviation = 0.0
    mean = 0.0
    valsum = 0.0
    for value in nums:
        mean += value
    mean = mean/len(nums)
    for value in nums:
        valsum += ((value-mean)**2)
    standardDeviation = (valsum/len(nums))**.5
    return round(standardDeviation,2)


