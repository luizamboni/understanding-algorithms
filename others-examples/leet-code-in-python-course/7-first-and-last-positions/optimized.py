nums = [10,11,11,11,14,15]


def find_first(nums, target):
    left_index = 0
    right_index = len(nums) - 1
    while left_index <= right_index:
        mid = (left_index + right_index) // 2
        print("find_the_first mid", mid, nums[mid])
        if nums[mid] == target:
            # if is the very first item or is not first occurrence
            if mid == 0 or nums[mid - 1] != target:
                return mid
            right_index = mid - 1
        elif nums[mid] > target:
            right_index = mid - 1
        else:
            left_index = mid + 1
    return -1

def find_last(nums, target):
    left_index = 0
    right_index = len(nums) - 1
    while left_index <= right_index:
        mid = (left_index + right_index) // 2
        # print("find_the_last mid", mid)
        if nums[mid] == target:
            # if is the very last item or is not last in contigous
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            left_index = mid + 1
        elif nums[mid] > target:
            right_index = mid - 1
        else:
            left_index = mid + 1
    return -1


def find_first_and_last(nums, target):
    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]


print(
    find_first_and_last(nums, 11),
)