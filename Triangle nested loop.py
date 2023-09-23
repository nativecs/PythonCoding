n=5
for rows in range(n):
    for space in range(rows,n):
        print(" ", end=' ')
    for space in range(rows+1):
        print("*",end=" ")
    print()

