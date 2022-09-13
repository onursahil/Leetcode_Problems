"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 
Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Constraints:

n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.
"""

def flipAndInvertImage(image):
    def flip(image):
        new_image = []
        for i in range(len(image)):
            new_image.append(image[i][::-1])
        
        return new_image
    
    def invert(image):
        new_image = []
        for i in range(len(image)):
            row = image[i]
            new_row = []
            for j in range(len(row)):
                if row[j] == 0:
                    new_row.append(1)
                if row[j] == 1:
                    new_row.append(0)
            new_image.append(new_row)
        
        return new_image
    
    flipped_image = flip(image)
    inverted_image = invert(flipped_image)
    
    return inverted_image

image = [[1,1,0],[1,0,1],[0,0,0]]
result = flipAndInvertImage(image)
print(result)