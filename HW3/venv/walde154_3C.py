def shortestDist(points):
    current = []
    distances = []
    distance = []
    if len(points) == 2:
        xsq = (points[0][0] - points[1][0])**2
        ysq = (points[0][1] - points[1][1])**2
        distance = (xsq+ysq)**.5
        return (distance)
    if len(points) > 2:
        for value in range(0,len(points),1):
            current = []
            workingpoints = []
            current = points[value]
            workingpoints += points
            workingpoints.remove(current)
            for value2 in workingpoints:
                xsq = (points[value][0] - value2[0]) ** 2
                ysq = (points[value][1] - value2[1]) ** 2
                distance = (xsq + ysq) ** .5
                distances.append(distance)
        return(round(min(distances),2))