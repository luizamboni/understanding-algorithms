
nums = [
    1,2,3,4,5,6,10,20,40,43,60
]

target = 60

def regular_search(nums, target):
    low = 0
    high = len(nums) - 1
    count_op = 0
    while high > low:
        count_op+=1
        if nums[low] == target:
            return low
        low += 1

    print("operations", count_op)
    return low


def binary_search(nums, target):
    low_index = 0
    high_index = len(nums) - 1

    count_op = 0

    while high_index >= low_index:

        count_op+=1
        mid_index = (low_index + high_index) // 2
        mid_value = nums[mid_index]
        
        if mid_value == target:
            print("operations", count_op)
            return mid_index
    
        if mid_value > target: # greater
            high_index = mid_index - 1
        if mid_value < target: # lower
            low_index = mid_index + 1
    
    print("operations", count_op)
    return None



print(
    regular_search(nums, target)
)


print(
    binary_search(nums, target)
)

