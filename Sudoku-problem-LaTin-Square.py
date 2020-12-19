from random import choice, shuffle
import random
import sys
random.seed(1)

def rls(n):
    if n <= 0:
        return []
    else:
        symbols = list(range(n))
        square = _rls(symbols)
        return _shuffle_transpose_shuffle(square)

def _shuffle_transpose_shuffle(matrix):
    square = matrix
    shuffle(square)
    trans =square    
    shuffle(trans)
    return trans

def _rls(symbols):
    n = len(symbols)
    if n == 1:
        return [symbols]
    else:
        sym = choice(symbols)
        symbols.remove(sym)
        square = _rls(symbols)
        square.append(square[0].copy())
        for i in range(n):
            square[i].insert(i, sym)
        return square

def _to_text(square):
    if square:
        width = max(len(str(sym)) for row in square for sym in row)
        txt = '\n'.join(' '.join(f"{sym:>{width}}" for sym in row)
                        for row in square)
    else:
        txt = ' '
    return txt

def _check(square): #Hàm kiểm tra Latin Square
    transpose = list(zip(*square))
    assert _check_rows(square) and _check_rows(transpose), \
        "Not a Latin square"
 
def _check_rows(square):
    if not square:
        return True
    set_row0 = set(square[0])
    return all(len(row) == len(set(row)) and set(row) == set_row0
               for row in square)

def transRow123(row):
    for i in range(0,9):
        if i==0 or i==1 or i==2:
            row[i]=base[0][0]*3 + row[i] + 1
        elif i==3 or i==4 or i==5:
            row[i]=base[0][1]*3 + row[i] + 1
        elif i==6 or i==7 or i==8:
            row[i]=base[0][2]*3 + row[i] + 1
        
    return row

def transRow456(row):
    for i in range(0,9):
        if i==0 or i==1 or i==2:
            row[i]=base[1][0]*3 + row[i] + 1
        elif i==3 or i==4 or i==5:
            row[i]=base[1][1]*3 + row[i] + 1
        elif i==6 or i==7 or i==8:
            row[i]=base[1][2]*3 + row[i] + 1
    
    return row
    
def transRow789(row):
    for i in range(0,9):
        if i==0 or i==1 or i==2:
            row[i]=base[2][0]*3 + row[i] + 1
        elif i==3 or i==4 or i==5:
            row[i]=base[2][1]*3 + row[i] + 1
        elif i==6 or i==7 or i==8:
            row[i]=base[2][2]*3 + row[i] + 1
    return row

def holes(grid, n):
    while n > 0:
        for i in range(9):
            if i == 0:
                i = random.randint(0, 2)
                j = random.randint(0, 2)
                while grid[i][j] == 0:
                    i = random.randint(0, 2)
                    j = random.randint(0, 2)
                grid[i][j] = 0
            elif i == 1:
                i = random.randint(0, 2)
                j = random.randint(3, 5)
                while grid[i][j] == 0:
                    i = random.randint(0, 2)
                    j = random.randint(3, 5)
                grid[i][j] = 0
            elif i == 2:
                i = random.randint(0, 2)
                j = random.randint(6, 8)
                while grid[i][j] == 0:
                    i = random.randint(0, 2)
                    j = random.randint(6, 8)
                grid[i][j] = 0
            elif i == 3:
                i = random.randint(3, 5)
                j = random.randint(0, 2)
                while grid[i][j] == 0:
                    i = random.randint(3, 5)
                    j = random.randint(0, 2)
                grid[i][j] = 0
            elif i == 4:
                i = random.randint(3, 5)
                j = random.randint(3, 5)
                while grid[i][j] == 0:
                    i = random.randint(3, 5)
                    j = random.randint(3, 5)
                grid[i][j] = 0
            elif i == 5:
                i = random.randint(3, 5)
                j = random.randint(6, 8)
                while grid[i][j] == 0:
                    i = random.randint(3, 5)
                    j = random.randint(6, 8)
                grid[i][j] = 0
            elif i == 6:
                i = random.randint(6, 8)
                j = random.randint(0, 2)
                while grid[i][j] == 0:
                    i = random.randint(6, 8)
                    j = random.randint(0, 2)
                grid[i][j] = 0
            elif i == 7:
                i = random.randint(6, 8)
                j = random.randint(3, 5)
                while grid[i][j] == 0:
                    i = random.randint(6, 8)
                    j = random.randint(3, 5)
                grid[i][j] = 0
            elif i == 8:
                i = random.randint(6, 8)
                j = random.randint(6, 8)
                while grid[i][j] == 0:
                    i = random.randint(6, 8)
                    j = random.randint(6, 8)
                grid[i][j] = 0
        n -= 1
    return output(_to_text(grid)) #hàm xuất kết quả  

def output(input):
    file = open('output.txt', 'w')
    file.write(input)
    file.close()
    lines = [line.rstrip('\n') for line in open('output.txt')]

def printBoard(bo):
    for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")
    
if __name__ == "__main__":            
    for i in [3]:
        square = rls(i) 
        square1= rls(i)
        square2= rls(i)
        square3= rls(i)
        square4= rls(i)
        square5= rls(i)
        square6= rls(i)
        square7= rls(i)
        square8= rls(i)

        for i in [square,square1,square2,square3,square4,square5,square6,square7,square8]:
            _to_text(i)
            _check(i)
        print('LaTin Square 3x3:\n')
        print(_to_text(square)) 
        print('\n')
        Square=[square,square1,square2,square3,square4,square5,square6,square7,square8]
        S=[]
        S.extend(square[0])
        S.extend(square1[0])
        S.extend(square2[0])
        S1=[]
        S1.extend(square[1])
        S1.extend(square1[1])
        S1.extend(square2[1])
        S2=[]
        S2.extend(square[2])
        S2.extend(square1[2])
        S2.extend(square2[2])
        S3=[]
        S3.extend(square3[0])
        S3.extend(square4[0])
        S3.extend(square5[0])
        S4=[]
        S4.extend(square3[1])
        S4.extend(square4[1])
        S4.extend(square5[1])
        S5=[]
        S5.extend(square3[2])
        S5.extend(square4[2])
        S5.extend(square5[2])
        S6=[]
        S6.extend(square6[0])
        S6.extend(square7[0])
        S6.extend(square8[0])
        S7=[]
        S7.extend(square6[1])
        S7.extend(square7[1])
        S7.extend(square8[1])
        S8=[]
        S8.extend(square6[2])
        S8.extend(square7[2])
        S8.extend(square8[2])
        S9=[S,S1,S2,S3,S4,S5,S6,S7,S8]
        random.shuffle(Square)
        grid=Square
        random.shuffle(grid)
        bo=S9

        print('Selection of Latin Square:')
        printBoard(bo)
        #Biến đổi cấu trúc hàng và cột để tạo ra bản laTin Square 9x9:
        #S là biến tạm s khi thực thi xong có thể đặt tên biến khác
        #Tiến hành phân chia kẻ ô cho dễ kiểm tra
        
        base=random.choice(grid)

        newRow1 = transRow123(S)
        newRow2 = transRow123(S1)
        newRow3 = transRow123(S2)
        newRow4 = transRow456(S3)
        newRow5 = transRow456(S4)
        newRow6 = transRow456(S5)
        newRow7 = transRow789(S6)
        newRow8 = transRow789(S7)
        newRow9 = transRow789(S8)

        sudogrid = [] #Generate a Grid
        sudogrid.append(newRow1)
        sudogrid.append(newRow2)
        sudogrid.append(newRow3)
        sudogrid.append(newRow4)
        sudogrid.append(newRow5)
        sudogrid.append(newRow6)
        sudogrid.append(newRow7)
        sudogrid.append(newRow8)
        sudogrid.append(newRow9)
        print('\nLatin Squaren Conversion To Base 10:')
        print(printBoard(sudogrid))
        print('\n')
        swap24 = sudogrid[1]
        sudogrid[1] = sudogrid[3]
        sudogrid[3] = swap24

        swap37 = sudogrid[2]
        sudogrid[2] = sudogrid[6]
        sudogrid[6] = swap37

        swap68 = sudogrid[5]
        sudogrid[5] = sudogrid[7]
        sudogrid[7] = swap68
        m=9  #Số Lỗ trong sudoku
        n=m/9 # Số lỗ trong mỗi matrix 3x3
        # Hàm điền số ngẫu nhiên vào bảng
        holes(S9, n) # hàm tạo lỗ trống
        


