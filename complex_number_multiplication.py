"""
A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Constraints:

num1 and num2 are valid complex numbers.
"""

def complexNumberMultiply(num1, num2):
    x1, y1 = num1[:-1].split('+')
    x1 = int(x1)
    y1 = int(y1)

    x2, y2 = num2[:-1].split('+')
    x2 = int(x2)
    y2 = int(y2)

    return str(x1*x2 - y1*y2)+"+"+str(x1*y2 + y1*x2)+"i"


num1, num2 = '1+-1i', '1+-1i'
num1, num2 = '1+-1i', '1+1i'
result = complexNumberMultiply(num1, num2)
print(result)
