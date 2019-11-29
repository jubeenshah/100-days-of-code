def maximumWater(height):
    if not height or len(height) == 1:
        return 0
    start = 0
    end = len(height) -1
    maxArea = float('-inf')
    while start != end:
        width = end - start
        area = width * min(height[start],height[end])
        print(area)
        if area > maxArea:
            maxArea = area
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return maxArea
        

maximumWater([1])