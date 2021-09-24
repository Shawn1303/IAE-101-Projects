# Shawn Zhu
# 114590303
# jiachzhu
#
# IAE 101 (Fall 2021)
# HW 2, Problem 5

def is_palindrome(s):
    c = []
    i = 0
    combine = ""
    for x in range(0,len(s)):
        if s[x] == " ":
            c.append(s[i:x])
            i = x+1
        c.append(s[i: ])
    for i in range(0, len(c)):
        combine += c[i]
    print(combine)  
    reverse = combine[len(combine): : -1]
    # c = s.replace(" ", "")
    # r = c[len(c): :-1]
    if combine == reverse:
        return True
    else:
        return False


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = is_palindrome("racecar")
    print("is_palindrome(\"racecar\") is:", test1)
    print()
    test2 = is_palindrome("raceboat")
    print("is_palindrome(\"raceboat\") is:", test2)
    print()
    test3 = is_palindrome("a man a plan a canal panama")
    print("is_palindrome(\"a man a plan a canal panama\") is:", test3)
    print()
    test4 = is_palindrome("a place to call up")
    print("is_palindrome(\"a place to call up\") is:", test4)
    print()
    test5 = is_palindrome("deified")
    print("is_palindrome(\"deified\") is:", test5)
    print()

