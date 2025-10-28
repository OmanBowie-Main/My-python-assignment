n = 5
for outer in range(n, 0, -1):
    for inner in range(5, outer - 1, -1):
        print(inner, end=" ")
    print()