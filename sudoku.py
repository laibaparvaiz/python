def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]
rows = []
for r in range(9):
    row = input()
    if len(row) != 9 or not row.isdigit():
        print("No")
        exit()
    rows.append(list(row))
ok = True
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break
if ok:
    for c in range(9):
        col = [rows[r][c] for r in range(9)]
        if not checkset(col):
            ok = False
            break
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(rows[r+i][c+j])
            if not checkset(square):
                ok = False
                break
if ok:
    print("Yes")
else:
    print("No")
