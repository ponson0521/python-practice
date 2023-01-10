# two sum
def twoSum(nums: list, target: int):
    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums:
            index_a = nums.index(a)
            if index_a != i:
                break 
    return sorted([i,index_a])   

nums = [1,2,3,4,5,6,7,8,9]
target = int(input("請輸入目標"))
print(twoSum(nums, target))    