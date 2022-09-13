def countBalls(lowLimit, highLimit):
    if lowLimit >= 1 and lowLimit <= highLimit and highLimit <= 10**5:
        boxes = {}
        for i in range(lowLimit, highLimit+1):
            total = sum([int(char) for char in str(i)])
            if str(total) not in boxes:
                boxes[str(total)] = 1
            else:
                boxes[str(total)] += 1
        
        print(boxes)
        
        return max(boxes.values())
    else:
        return False

lowLimit, highLimit = 5, 13
result = countBalls(lowLimit, highLimit)
print(result)