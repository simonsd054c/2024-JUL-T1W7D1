# Input numerator as n and denominator as d
n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))

# If d is 0
if d == 0:
    # display "denominator cannot be zero"
    print("Denominator cannot be zero")

# else
else:
    # Calculate q = n / d
    q = n / d
    # display q
    print(q)