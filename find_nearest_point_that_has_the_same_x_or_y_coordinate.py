"""
You are given two integers, x and y, which represent your current location on a 
Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] 
represents that a point exists at (ai, bi). A point is valid if it shares the same 
x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. 
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Example 1:

Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, 
[2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. 
[2,4] has the smallest index, so return 2.

Example 2:

Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:

Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.

Constraints:

1 <= points.length <= 104
points[i].length == 2
1 <= x, y, ai, bi <= 104
"""

def nearestValidPoint(x, y, points):
    minimum_number = float('inf')
    common_points = []
    manhattan_distances = []
    for i in range(len(points)):
        x_point = points[i][0]
        y_point = points[i][1]

        if x_point == x or y_point == y:
            common_points.append([x_point, y_point])
            manhattan_distances.append(abs(x - x_point) + abs(y - y_point))
    
    if len(manhattan_distances) == 0:
        return -1
    else:
        for i in range(len(manhattan_distances)):
            if manhattan_distances[i] < minimum_number:
                minimum_number = manhattan_distances[i]
                print(minimum_number)
                min_coord = common_points[i]

    return points.index(min_coord)

x, y, points = 3, 4, [[2,3]]
result = nearestValidPoint(x, y, points)
print(result)