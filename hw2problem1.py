# Shawn Zhu
# 114590303
# jiachzhu
#
# IAE 101 (Fall 2021)
# HW 2, Problem 1

def divisible(n):
    divisibility = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in numbers:
        if n % item == 0:
            divisibility.append(True)
        else:
            divisibility.append(False)
    return divisibility # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = divisible(126)
    print("divisible(126) is:", test1)
    print()
    test2 = divisible(20)
    print("divisible(20) is:", test2)
    print()
    test3 = divisible(1024)
    print("divisible(1024) is:", test3)
    print()
    test4 = divisible(17)
    print("divisible(17) is:", test4)
    print()
    test5 = divisible(539)
    print("divisible(539) is:", test5)
    print()

