"""
Defanging and IP Address


Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".


Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


Constraints:

- The given address is a valid IPv4 address.

"""

def defangIPaddr(address):
    return address.replace('.', '[.]')

address = "255.100.50.0"
result = defangIPaddr(address)
print(result)