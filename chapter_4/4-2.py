data = input()

row = int(ord(data[0]))-int(ord('a'))
column = int(data[1])-1

plans = [(2, -1), (2, 1), (-2, -1), (-2, 1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

moves = 0

for plan in plans:
    new_row = row + plan[1]
    new_column = column + plan[0]

    if new_column < 0 or new_column > 7 or new_row < 0 or new_row > 7:
        continue

    moves += 1
    print(new_row, new_column)

print(moves)

