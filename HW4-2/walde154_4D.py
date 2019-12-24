def checkSudoku(matrix):
    flag = True
    for line in matrix: #Checks Row
        check = {}
        for value in line:
            if value not in check:
                check[value] = 1
            else:
                check[value] += 1
        if max(check.values()) != 1:
            flag = False

    for row in range(0,9,1): #Checks Columns
        check = {}
        for column in range(0,9,1):
            if matrix[row][column] not in check:
                check[matrix[row][column]] = 1
            else:
                check[matrix[row][column]] += 1
        if max(check.values()) != 1:
            flag = False

    sq1 = {}
    sq2 = {}
    sq3 = {}
    sq4 = {}
    sq5 = {}
    sq6 = {}
    sq7 = {}
    sq8 = {}
    sq9 = {}

    for matrixcol in range(0,3,1): #Checks Squares
        if matrixcol == 0:
            for i in range(0, 9, 1):
                if i < 3:
                    for x in range(0,3,1):
                        if matrix[i][x] not in sq1:
                            sq1[matrix[i][x]] = 1
                        else:
                            sq1[matrix[i][x]] += 1
                if max(check.values()) != 1:
                    flag = False
                if i >= 3 and 6 > i :
                    for x in range(0, 3, 1):
                        if matrix[i][x] not in sq2:
                            sq2[matrix[i][x]] = 1
                        else:
                            sq2[matrix[i][x]] += 1
                if max(check.values()) != 1:
                    flag = False
                if i >= 6 and 9 > i :
                    for x in range(0, 3, 1):
                        if matrix[i][x] not in sq3:
                            sq3[matrix[i][x]] = 1
                        else:
                            sq3[matrix[i][x]] += 1
                if max(check.values()) != 1:
                    flag = False
        if matrixcol == 1:
            for i in range(0, 9, 1):
                if i < 3:
                    for x in range(0, 3, 1):
                        if matrix[i][x+3] not in sq4:
                            sq4[matrix[i][x+3]] = 1
                        else:
                            sq4[matrix[i][x+3]] += 1
                if max(check.values()) != 1:
                    flag = False
                if i >= 3 and 6 > i:
                    for x in range(0, 3, 1):
                        if matrix[i][x+3] not in sq5:
                            sq5[matrix[i][x+3]] = 1
                        else:
                            sq5[matrix[i][x+3]] += 1
                if max(check.values()) != 1:
                    flag = False
                if i >= 6 and 9 > i:
                    for x in range(0, 3, 1):
                        if matrix[i][x+3] not in sq6:
                            sq6[matrix[i][x+3]] = 1
                        else:
                            sq6[matrix[i][x+3]] += 1
                if max(check.values()) != 1:
                    flag = False
        if matrixcol == 2:
            for i in range(0, 9, 1):
                if i < 3:
                    for x in range(0, 3, 1):
                        if matrix[i][x + 6] not in sq7:
                            sq7[matrix[i][x + 6]] = 1
                        else:
                            sq7[matrix[i][x + 6]] += 1
                if max(check.values()) != 1:
                    flag = False
                if i >= 3 and 6 > i:
                    for x in range(0, 3, 1):
                        if matrix[i][x + 6] not in sq8:
                            sq8[matrix[i][x + 6]] = 1
                        else:
                            sq8[matrix[i][x + 6]] += 1
                if max(check.values()) != 1:
                    flag = False
                if i >= 6 and 9 > i:
                    for x in range(0, 3, 1):
                        if matrix[i][x + 6] not in sq9:
                            sq9[matrix[i][x + 6]] = 1
                        else:
                            sq9[matrix[i][x + 6]] += 1
                if max(check.values()) != 1:
                    flag = False

    return flag
