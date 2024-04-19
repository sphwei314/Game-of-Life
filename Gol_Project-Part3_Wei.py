MAX_ROW = 40
MAX_COL = 80

currentGen = [[0]*(MAX_COL) for row in range(MAX_ROW)]

tempGen = [[0]*(MAX_COL) for row in range(MAX_ROW)]

def displayMenu ():
    print ("U - Press 'U' to load the 'U' pattern.\n"
           "Play - Press 'P' to play the game.\n"
           "Stop - Press 'S' to stop the game.\n"
           "Clear - Press 'C' to clear the grid.\n"
           "Manual - Press 'M' to enter into a Manual mode.\n"
           "Save - Press 'Z' to save the current live cell pattern of the currentArray to a file.\n"
           "Load - Press 'L' to load a saved file along with the saved pattern and its numbers of rows and columns.\n")

def setZeroList(any_list):
    for row in range(len(any_list)):
        for col in range(len(any_list[row])):
            any_list[row][col]=0

from random import randint
def setInitialPatternList(any_list):
    a = randint(0,len(any_list)-6)  # row
    b = randint(0,len(any_list[0])-7)  # column

    any_list[a][b] = 1
    any_list[a][b + 6] = 1
    any_list[a + 1][b] = 1
    any_list[a + 2][b] = 1
    any_list[a + 3][b] = 1
    any_list[a + 4][b] = 1
    any_list[a + 5][b] = 1
    any_list[a + 1][b + 6] = 1
    any_list[a + 2][b + 6] = 1
    any_list[a + 3][b + 6] = 1
    any_list[a + 4][b + 6] = 1
    any_list[a + 5][b + 6] = 1
    any_list[a + 5][b + 5] = 1
    any_list[a + 5][b + 4] = 1
    any_list[a + 5][b + 3] = 1
    any_list[a + 5][b + 2] = 1
    any_list[a + 5][b + 1] = 1

def copylist(any_list, copied_any_list):
    for row in range(len(copied_any_list)):
        for col in range(len(copied_any_list[row])):
            copied_any_list[row][col] = any_list[row][col]

def displayList(any_list):
    for row in range(len(any_list)):
        for col in range(len(any_list[row])):
            print(any_list[row][col], end=' ')
        print()

def isValidSpot(row, col):
    if 0 <= row < MAX_ROW:
        if 0 <= col < MAX_COL:
            return True
    return False

def counter():
    for row in range(len(tempGen)):
        for col in range(len(tempGen[row])):
            neighborCount = 0
            if isValidSpot(row, col) and currentGen[row][col] == 1:
                if isValidSpot(row-1, col-1) and currentGen[row-1][col-1] == 1:
                    neighborCount += 1
                if isValidSpot(row-1, col) and currentGen[row-1][col] == 1:
                    neighborCount += 1
                if isValidSpot(row-1, col+1) and currentGen[row-1][col+1] == 1:
                    neighborCount += 1
                if isValidSpot(row, col-1) and currentGen[row][col-1] == 1:
                    neighborCount += 1
                if isValidSpot(row, col+1) and currentGen[row][col+1] == 1:
                    neighborCount += 1
                if isValidSpot(row+1, col-1) and currentGen[row+1][col-1] == 1:
                    neighborCount += 1
                if isValidSpot(row+1, col) and currentGen[row+1][col] == 1:
                    neighborCount += 1
                if isValidSpot(row+1, col+1) and currentGen[row+1][col+1] == 1:
                    neighborCount += 1
                if neighborCount < 2:
                    tempGen[row][col] = 0
                if neighborCount == 2 or neighborCount == 3:
                    tempGen[row][col] = 1
                if neighborCount > 3:
                    tempGen[row][col] = 0
            elif isValidSpot(row, col) and currentGen[row][col] == 0:
                if isValidSpot(row-1, col-1) and currentGen[row - 1][col - 1] == 1:
                    neighborCount += 1
                if isValidSpot(row-1, col) and currentGen[row - 1][col] == 1:
                    neighborCount += 1
                if isValidSpot(row-1, col+1) and currentGen[row - 1][col+1] == 1:
                    neighborCount += 1
                if isValidSpot(row, col-1) and currentGen[row][col - 1] == 1:
                    neighborCount += 1
                if isValidSpot(row, col+1) and currentGen[row][col+1] == 1:
                    neighborCount += 1
                if isValidSpot(row+1, col-1) and currentGen[row+1][col - 1] == 1:
                    print('14 ' + str(row)+' '+ str(col))
                    neighborCount += 1
                if isValidSpot(row+1, col) and currentGen[row+1][col] == 1:
                    neighborCount += 1
                if isValidSpot(row+1, col+1) and currentGen[row+1][col+1] == 1:
                    neighborCount += 1
                if neighborCount == 3:
                    tempGen[row][col] = 1

def setBlinker(any_list):
    a = randint(0, len(any_list) -1) # row
    b = randint(0, len(any_list[0]) - 3) #column

    with open('blinker.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            row, col = line.split()
            row_int = int(row)
            col_int = int(col)
            any_list[a+row_int][b+col_int] = 1

def setBoat(any_list):
    a = randint(0, len(any_list) -2) # row
    b = randint(0, len(any_list[0]) - 2) #column

    with open('boat.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            row, col = line.split()
            row_int = int(row)
            col_int = int(col)
            any_list[a + row_int][b + col_int] = 1

def setGlider(any_list):
    a = randint(0, len(any_list) - 3) # row
    b = randint(0, len(any_list[0]) - 3) #column

    with open('glider.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            row, col = line.split()
            row_int = int(row)
            col_int = int(col)
            any_list[a + row_int][b + col_int] = 1

def manualMode():
    print("Enter MAX_ROW: ")
    global MAX_ROW
    MAX_ROW = int(input(">>"))
    print("Enter MAX_COL: ")
    global MAX_COL
    MAX_COL = int(input(">>"))

    global currentGen
    currentGen = [[0] * (MAX_ROW) for col in range(MAX_COL)]
    global tempGen
    tempGen = [[0] * (MAX_ROW) for col in range(MAX_COL)]

    print("blinker - Press '1' to load the pattern.\n"
          "boat - Press '2' to load the pattern.\n"
          "glider - Press '3' to load the pattern.")
    userinput = input(">>")

    if userinput == '1':
        setZeroList(tempGen)
        setZeroList(currentGen)
        setBlinker(tempGen)
        copylist(tempGen, currentGen)
        displayList(currentGen)

    if userinput == '2':
        setZeroList(tempGen)
        setZeroList(currentGen)
        setBoat(tempGen)
        copylist(tempGen, currentGen)
        displayList(currentGen)

    if userinput == '3':
        setZeroList(tempGen)
        setZeroList(currentGen)
        setGlider(tempGen)
        copylist(tempGen, currentGen)
        displayList(currentGen)

displayMenu()
displayList(currentGen)

while(True):
    userinput = input(">>")
    if userinput.lower() == "u":
        setZeroList(tempGen)
        setInitialPatternList(tempGen)
        copylist(tempGen, currentGen)
        displayList(currentGen)
    elif userinput.lower() == "p":
        counter()
        copylist(tempGen, currentGen)
        displayList(currentGen)
        continue
    elif userinput.lower() == "c":
        setZeroList(tempGen)
        setZeroList(currentGen)
        displayList(currentGen)
    elif userinput.lower() == "s":
        break
    elif userinput.lower() == "m":
        manualMode()
    elif userinput.lower() == "z":
        print("Type file name:")
        file_name = str(input(">>")) + '.txt'
        with open(file_name,'w') as f:
            for row in range(len(currentGen)):
                for col in range(len(currentGen[row])):
                    if currentGen[row][col] == 1:
                        row_string = str(currentGen[row])
                        col_string = str(currentGen[col])
                        coordinates = '{0} {1}'.format(row, col)
                        f.write(coordinates+'\n')

    elif userinput.lower() == "l":
        print("Type file load name:")
        load_name = str(input(">>")) + '.txt'
        with open(load_name,'r') as f:
            lines = f.readlines()
            for line in lines:
                row, col = line.split()
                row_int = int(row)
                col_int = int(col)
                tempGen[row_int][col_int] = 1
        displayList(tempGen)
