# Enter your code here. Read input from STDIN. Print output to STDOUT
def queuesUsingStack(query, nums):
    if query[0] == 1:
        nums.append(query[1])
        #print(nums)
    elif query[0] == 2:
        nums = nums[1:]
        #print(nums)
    else:
        print(nums[0])
    return nums

numberOfQueries = int(input())
nums = []
for _ in range(numberOfQueries):
    query = list(map(int,input().split(" ")))
    nums = queuesUsingStack(query,nums)
