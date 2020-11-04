import random
#from random import randint, shuffle

#random.seed(2)  # Giả lập random lưu kết quả cố định với hệ số m

# Tạo bảng 9X9
grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

# Kiểm tra bảng 9X9
def checkGrid(grid):
  for row in range(0, 9):
      for col in range(0, 9):
        if grid[row][col] == 0:
          return False
  return True

#Thêm phần tử vào bảng
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]  #Hàm shuffle dùng để đổi ngẫu nhiên thứ tự của các phần tử trong chuỗi
def fillGrid(grid):
  global counter
  for i in range(0, 81):
    row = i//9
    col = i % 9
    if grid[row][col] == 0:
      random.shuffle(numberList)
      for value in numberList:
        if not(value in grid[row]):
          if not value in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
            square = []
            if row < 3:
              if col < 3:
                square = [grid[i][0:3] for i in range(0, 3)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(0, 3)]
              else:
                square = [grid[i][6:9] for i in range(0, 3)]
            elif row < 6:
              if col < 3:
                square = [grid[i][0:3] for i in range(3, 6)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(3, 6)]
              else:
                square = [grid[i][6:9] for i in range(3, 6)]
            else:
              if col < 3:
                square = [grid[i][0:3] for i in range(6, 9)]
              elif col < 6:
                square = [grid[i][3:6] for i in range(6, 9)]
              else:
                square = [grid[i][6:9] for i in range(6, 9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col] = value
              if checkGrid(grid):
                return True
              else:
                if fillGrid(grid):
                  return True
      break
  grid[row][col] = 0


#Tạo lỗ trống
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
    return grid

# coverter chuỗi thành bảng 9X9
def _to_text(square):
    if square:
        width = max(len(str(sym)) for row in square for sym in row)
        txt = '\n'.join(' '.join(f"{sym:>{width}}" for sym in row)
                        for row in square)
    else:
        txt = ''
    return txt

# Xuất ra file test.txt



def output(input):
    file = open('output.txt', 'w')
    file.write(input)
    file.close()
    lines = [line.rstrip('\n') for line in open('output.txt')]



if __name__ == "__main__":
    m=45  #Số Lỗ trong sudoku
    n=m/9 # Số lỗ trong mỗi matrix 3x3
    fillGrid(grid) # Hàm điền số ngẫu nhiên vào bảng
    holes(grid, n) # hàm tạo lỗ trống
    output(_to_text(grid)) #hàm xuất kết quả

