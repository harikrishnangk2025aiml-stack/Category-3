board = [0, 4, 7, 5, 2, 6, 1, 3]
def conflicts(b):
    c = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(b[i] - b[j]) == abs(i - j):
                c += 1
    return c
print("Conflicts:", conflicts(board))
if conflicts(board) == 0:
    print("Solution Found")
else:
    print("Local Optimum")
