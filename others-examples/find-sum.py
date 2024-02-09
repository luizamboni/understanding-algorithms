
nums = [1, 2, 4, 5, 5]
target = 7

def find_sum_brute(nums, target):
    left1 = 0
    right1 = len(nums) - 1
    while left1 <= right1:
        left2 = 0
        right2 = len(nums) - 1
        while left2 <= right2:
            if nums[left1] + nums[left2] == target:
                return left1, left2
            print(nums[left1], nums[left2])
            left2+=1
        left1 +=1

def find_sum_optimized(nums, target):
    left1 = 0
    right1 = len(nums) - 1
    while left1 <= right1:
        left2 = 0
        right2 = len(nums) - 1
        while left2 <= right2:
            if nums[left1] + nums[left2] == target:
                return left1, left2
            print(nums[left1], nums[left2])
            left2+=1
        left1 +=1


find_sum_brute(nums, target)



find_sum_optimized(nums, target)

