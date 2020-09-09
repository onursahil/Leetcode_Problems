"""

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 
for its first and second level revision number. Its third and fourth level revision number are both 0.


Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1


Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1


Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1


Example 4:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”


"""

def compareVersion(version_1, version_2):
    len_diff = abs(len(version_1) - len(version_2)) // 2

    if len_diff != 0:
        extra = ".0" * len_diff
        if len(version_1) > len(version_2):
            version_2 += extra
        else:
            version_1 += extra
    
    v1_list = version_1.split(".")
    v2_list = version_2.split(".")
    

    min_len = 0
    if len(v1_list) < len(v2_list):
        min_len = len(v1_list)
    else:
        min_len = len(v2_list)

    for i in range(min_len):
        if int(v1_list[i]) > int(v2_list[i]):
            return 1
        elif int(v1_list[i]) < int(v2_list[i]):
            return -1
        else:
            continue
    answer = 0

    return answer


version_1, version_2 = "7.5.2.4", "7.5.3"
result = compareVersion(version_1, version_2)
print(result)