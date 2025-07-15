c0 = int(input("Enter a natural number (non-zero): "))

if c0 <= 0:
    print("The number must be a natural number (positive integer).")
else:
    steps = 0
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
    print(c0)  
    print("Steps:", steps)
