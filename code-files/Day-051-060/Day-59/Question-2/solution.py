def trappingRainWater(height):
    ans = 0
    l,r = 0 , len(height) -1
    l_max, r_max = 0,0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= l_max:
                l_max = height[l]
            else:
                ans += l_max - height[l]
            l += 1
        else:
            if height[r] >= r_max:
                r_max = height[r]
            else:
                ans += r_max - height[r]
            r -= 1
    return ans

trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1])