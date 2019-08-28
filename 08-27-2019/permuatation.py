def permutation(nums):
    res = []
    n = len(nums)
    def helper(nums, res, path):
        if len(path) == n:
            res.append("".join(path))
        for i in range(len(nums)):
            helper(nums[:i]+nums[i+1:], res, path+[nums[i]])
    helper(nums, res, [])
    return res
nums = "lis"
print(permutation(nums))