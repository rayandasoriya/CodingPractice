def next_permuation(nums):
    N=len(nums)
    for i in range(N-1,0,-1):
        if nums[i]>nums[i-1]:
            print(i)
            for j in range(N-1,i-1,-1):
                print(j,i-1)
                if nums[j]>nums[i-1]:
                    nums[j],nums[i-1]=nums[i-1],nums[j]
                    nums[i:]=sorted(nums[i:]) 
                    return
    nums.sort()
nums = [1,9,6,2,1]
next_permuation(nums)
print(nums)