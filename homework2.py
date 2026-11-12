number=int(input("number: "))
working=number
digits=0
total=0
reversed_number=0

if working==0:
    digits=1
else:
    while working > 0:
        last_digit = working % 10
        total = total + last_digit
        reversed_number = (reversed_number * 10) + last_digit
        digits += 1
        working = working // 10

print(f"Digits: {digits}")
print(f"Digit sum: {total}")
print(f"Reversed: {reversed_number}")