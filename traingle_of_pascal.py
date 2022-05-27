def PrintPasTriangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0]+row, row+[0])]

rows = int(input())
if rows == 0:
    print([1])
PrintPasTriangle(rows)