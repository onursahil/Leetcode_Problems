"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 
Constraints:

0 <= x <= 231 - 1
"""

"""
EXPLANATION

1. Take a reasonable guess (approximate root) for the square root.
2. Add the approximate root with the original number divided by the approximate root and divide by 2.
   x_i := (x_i + n / x_i) / 2
3. Continue step 2 until the difference in the approximate root along the iterations is less than the desired value (or precision value).
4. The approximate root is the square root we want.
"""

def mySqrt(x):
    r = x
    precision = 10 ** (-10)
    print(precision)

    while abs(x - r * r) > precision:
        r = (r + x / r) / 2

    return int(r)

x = 44
result = mySqrt(x)
print(result)