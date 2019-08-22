#https://leetcode.com/problems/jump-game-ii/submissions/

def jump(nums):
    curr_max = 0
    next_max = 0
    steps = 0
    n  = len(nums)
    
    for i in range(n):
        if curr_max < i:
            steps += 1
            curr_max = next_max
        next_max = max(next_max, nums[i]+i)
    return steps

print(jump([2,3,1,1,4,1]))