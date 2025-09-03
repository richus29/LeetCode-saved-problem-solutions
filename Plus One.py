digits = [9]

digits = list(map(int,(str(int("".join(map(str,digits))) + 1))))


"""
digits[len(digits)-1] = digits[len(digits)-1] + 1
for i in range(len(digits)-1,-1,-1):
    if digits[i] == 10:
        digits[i] = 0
        digits[i-1] = digits[i-1] +1"""

print(digits)