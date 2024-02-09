
# nums = [2,4,1,7]
nums = [1,2,4,7]
target = 11

def find_sum_brute(nums, target):
    left1 = 0
    right1 = len(nums) - 1
    count = 0
    while left1 <= right1:
        left2 = 0
        right2 = len(nums) - 1
        while left2 <= right2:
            count += 1
            print("operations count", count, "comparing", left1, "against", left2)

            if nums[left1] + nums[left2] == target:
                return left1, left2
            left2+=1
        left1 +=1

def find_sum_optimized(nums, target):
    left1 = 0
    right1 = len(nums) - 1
    count = 0
    while left1 <= right1:
        # the second pointer is always after a first point
        left2 = left1 + 1
        right2 = len(nums) - 1
        while left2 <= right2:
            count += 1
            print("operations count", count, "comparing", left1, "against", left2)
            if nums[left1] + nums[left2] == target:
                return left1, left2
            left2+=1
        left1 +=1


print("find_sum_brute")
find_sum_brute(nums, target)


print("find_sum_optimized")
find_sum_optimized(nums, target)

