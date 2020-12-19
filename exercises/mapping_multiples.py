# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".
i = 1
while i < 101:
    if i in range(0, 101, 15):
        print("FizzBuzz")
        i += 1
        continue
    elif i in range(0, 101, 3):
        print("Fizz")
        i += 1
        continue
    elif i in range(0, 101, 5):
        print("Buzz")
        i += 1
        continue
    else:
        print(i)
        i += 1

"""
Alternate Solution:

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

"""
