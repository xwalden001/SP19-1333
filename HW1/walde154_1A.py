def BMI(pounds,inches):
    kg = float(pounds) * 0.4536
    meters = (inches/12)*0.3048
    bmindex =float(kg/(meters)**2)
    return bmindex
