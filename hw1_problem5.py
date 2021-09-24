# Shawn Zhu
# 114590303
# jiachzhu
#
# IAE 101 (Fall 2021)
# HW 1, Problem 5

def how_long(distance, fraction, scale):
    c = 186000
    # ADD YOUR CODE HERE
    speed = distance/(fraction*c)
    if scale == "M" :
        speed = speed / 60
    elif scale == "H" :
        speed = speed / (60**2)
    elif scale == "D" :
        speed = speed / ((60**2)*24)
    elif scale == "Y" :
        speed = speed / ((60**2)*24*365)
    return speed # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = how_long(238900, 0.01, "M") # approximate distance to Moon
    print("how_long(238900, 0.01, 'M') is:", test1)
    print()
    test2 = how_long(45594000, 0.01, "H") # approximate distance to Mars
    print("how_long(45594000, , 0.01, 'H') is:", test2)
    print()
    test3 = how_long(93000000, 1.0, "M") # approximate distance to Sun
    print("how_long(93000000, 1.0, 'M') is:", test3)
    print()
    test4 = how_long(9000000000, 0.01, "D") # approximate distance to edge of Solar System
    print("how_long(9000000000, 0.01, 'D') is:", test4)
    print()
    test5 = how_long(25000000000000, 0.01, "Y") # approximate distance to closest system Alpha Centauri
    print("how_long(25000000000000, 0.01, 'Y') is:", test5)
    print()

