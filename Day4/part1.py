def main():
    file = open("Day4/input.txt", "r")
    wordsearch = []
    words = 0
    for line in file:
        wordsearch.append(list(line.strip()))

    row = 0
    while row < len(wordsearch):
        col = 0
        currRow = wordsearch[row]
        while col < len(currRow):
            if currRow[col] == 'X':
                canGoBackwards = col - 3 > 0
                canGoUp = row - 3 > 0
                canGoFowards = col + 3 < len(currRow)
                canGoDown = row + 3 < len(wordsearch)

                if canGoBackwards:
                    if CheckBackwards(currRow, col):
                        words += 1
                if canGoDown:
                    if CheckDown(wordsearch, row, col):
                        words += 1
                if canGoFowards:
                    if CheckFowards(currRow, col):
                        words += 1
                if canGoUp:
                    if CheckUp(wordsearch, row, col):
                        words += 1
                if canGoUp and canGoBackwards:
                    if CheckBackDiagonalUp(wordsearch, row, col):
                        words += 1
                if canGoUp and canGoFowards:
                    if CheckForwardDiagonalUp(wordsearch, row, col):
                        words += 1
                if canGoDown and canGoBackwards:
                    if CheckBackDiagonalDown(wordsearch, row, col):
                        words += 1
                if canGoDown and canGoFowards:
                    if CheckForwardDiagonalDown(wordsearch, row, col):
                        words += 1
            col += 1
        row += 1
    print(words)


def CheckBackwards(row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if row[col - i] == check[i]:
            i += 1
        else:
            return False
    return True

def CheckFowards(row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if row[col + i] == check[i]:
            i += 1
        else:
            return False
    return True
    
def CheckUp(wordsearch, row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if wordsearch[row-i][col] == check[i]:
            i+=1
        else:
            return False
    return True

def CheckDown(wordsearch, row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if wordsearch[row+i][col] == check[i]:
            i+=1
        else:
            return False
    return True

def CheckBackDiagonalUp(wordsearch, row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if wordsearch[row-i][col-i] == check[i]:
            i+=1
        else:
            return False
    return True

def CheckForwardDiagonalUp(wordsearch, row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if wordsearch[row-i][col+i] == check[i]:
            i+=1
        else:
            return False
    return True

def CheckBackDiagonalDown(wordsearch, row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if wordsearch[row+i][col-i] == check[i]:
            i+=1
        else:
            return False
    return True

def CheckForwardDiagonalDown(wordsearch, row, col):
    check = ["X", "M", "A", "S"]
    i = 1
    while i <= 3:
        if wordsearch[row+i][col+i] == check[i]:
            i+=1
        else:
            return False
    return True
            

main()