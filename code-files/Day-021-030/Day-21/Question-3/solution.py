def findMedianSortedArrays(nums1, nums2) -> float:
    nums1 = (nums1+nums2)
    nums1.sort()
    print(nums1)
    if len(nums1) % 2 != 0:
        return nums1[len(nums1)//2]
    else:
        print(nums1[(len(nums1)-1)//2],nums1[(len(nums1)//2)] )
        return (nums1[(len(nums1)-1)//2]+ nums1[(len(nums1)//2)])/2
    print(nums1)
findMedianSortedArrays([1,2,3],[4,5,6])