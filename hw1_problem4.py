# Shawn Zhu
# 114590303
# jiachzhu
#
# IAE 101 (Fall 2021)
# HW 1, Problem 4

def temp_converter(temperature, f_or_c):
    # ADD YOUR CODE HERE
    if f_or_c == "C":
        convert = (temperature - 32)*5/9
    else :
        convert = 9*temperature/5+32
    return convert # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("temp_converter(100,'C') is", temp_converter(100, 'C'))
    print()
    print("temp_converter(0,'F') is", temp_converter(0, 'F'))
    print()
    print("temp_converter(212,'C') is", temp_converter(212, 'C'))
    print()
    print("temp_converter(32,'C') is", temp_converter(32, 'C'))
    print()
    print("temp_converter(50,'F') is", temp_converter(50, 'F'))
    print()
