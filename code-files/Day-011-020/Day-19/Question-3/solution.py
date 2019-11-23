def mergeSortedArrays(nums1: list, nums2:list, m:int,n:int):
    nums1 = nums1[:m]+nums2[:n]
    nums1.sort()
    print(nums1)
            

mergeSortedArrays([1,2,3,0,0,0], [2,5,6],3,3)