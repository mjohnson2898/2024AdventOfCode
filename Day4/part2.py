def main():
    file = open("Day4/input.txt", "r")
    wordsearch = []
    words = 0
    for line in file:
        wordsearch.append(list(line.strip()))

    row = 1
    while row < len(wordsearch) - 1:
        col = 1
        while col < ( len(wordsearch[row]) - 1 ):
            currRow = wordsearch[row]
            if currRow[col] == 'A':
                left = checkBackSlash(wordsearch, row, col)
                right = checkForwardSlash(wordsearch, row, col)
                if left and right:
                    words += 1
            col += 1
        row += 1
    print(words)
                

def checkBackSlash(wordsearch, row, col):
    if wordsearch[row - 1][col - 1] == 'M' and wordsearch[row + 1][col + 1] == 'S' :
        return True
    elif wordsearch[row - 1][col - 1] == 'S' and wordsearch[row + 1][col + 1] == 'M' :
        return True
    else:
        return False
    

def checkForwardSlash(wordsearch, row, col):
    if wordsearch[row - 1][col + 1] == 'M' and wordsearch[row + 1][col - 1] == 'S' :
        return True
    elif wordsearch[row - 1][col + 1] == 'S' and wordsearch[row + 1][col - 1] == 'M' :
        return True
    else:
        return False

main()