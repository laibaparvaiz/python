Date_of_birth = input("Enter your DOB(YYYYMMDD): ")
total = 0
for digit in Date_of_birth:
    if digit.isdigit():
       total += int(digit)
while total > 9:
        total_str = str(total)
        new_total = 0
        for d in total_str:
            new_total += int(d)
        total = new_total
print("Final result:", total)
