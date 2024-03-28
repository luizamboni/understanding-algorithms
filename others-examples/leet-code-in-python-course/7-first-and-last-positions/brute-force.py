nums = [ 10,11,11,11,14,15]

def find_first(nums, target):
    for index in range(0, len(nums) - 1):
        if nums[index] == target:
            return index
    return -1

def find_last(nums, target):
    for index in range(len(nums) - 1, -1, -1):
        if nums[index] == target:
            return index
    return -1


def find_first_and_last(nums, target):
    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]


print(
    find_first_and_last(nums, 11)
)