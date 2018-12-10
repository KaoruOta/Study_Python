# The preferred 'pythonic' way to create a list
numbers_0_to_9 = [x for x in range(10)]
print("Numbers 0 to 9", numbers_0_to_9)

# The above is equivalent to the following just more compact:
numbers_0_to_9 = []
for x in range(10):
    numbers_0_to_9.append(x)
print("Numbers 0 to 9", numbers_0_to_9)

# You can also choose to do computation / flow control when generating
# lists
squares = [x * x for x in range(10)]
print("Squares       ", squares)

# note - this example uses the "modulo" operator
odds = [x for x in range(10) if x % 2 == 1]
print("Odds          ", odds)
