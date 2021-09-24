
#
# IAE 101 (Fall 2021)
# HW 1, Problem 2

def tip_amount(bill, good_service):
    # ADD YOUR CODE HERE
    tip = 0
    if (bill <= 25.00): 
        tip = 6.00
    elif (good_service):
        tip = 0.27*bill
    else :
        tip = 0.13*bill
    
    return tip # CHANGE OR REMOVE THIS LINE


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("tip_amount(23.37,True) is", tip_amount(23.37, True))
    print()
    print("tip_amount(23.37,False) is", tip_amount(23.37, False))
    print()
    print("tip_amount(81.75,True) is", tip_amount(81.75, True))
    print()
    print("tip_amount(63.59,True) is", tip_amount(63.59, True))
    print()
    print("tip_amount(63.59,False) is", tip_amount(63.59, False))
    print()
