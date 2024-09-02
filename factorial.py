# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Input number as num from user
num = int(input("Enter a number to calculate its factorial: "))

# Initialise i = 1
# i = 1

# Initialise fact = 1
fact = 1

# Loop until i <= num
# while i <= num:
for i in range(1, num + 1):
    # fact = fact * i
    # fact = fact * i
    fact *= i
    # i = i + 1
    # i = i + 1

# display fact
print(fact)