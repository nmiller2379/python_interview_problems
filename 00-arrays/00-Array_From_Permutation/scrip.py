def buildArray(nums):
    ans = []
    for num in range(len(nums)):
        to_push = nums[num]
        ans.append(nums[to_push])
    return ans

result = buildArray([0,2,1,5,3,4])
result_1 = buildArray([0])
print(result)
print(result_1)
