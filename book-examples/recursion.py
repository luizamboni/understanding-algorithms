
nums = [ 222,10,52]


def suma(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        item = arr.pop()
        return suma(arr) + item
    


def cardinality(arr):
    if len(arr) == 1:
        return 1
    else:
        arr.pop()
        return cardinality(arr) + 1

def maximum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        item = arr.pop()
        return item if item > maximum(arr.copy()) else maximum(arr.copy())


# doesn't make much sense because the target is exactly the seme item of element, 
# but imagine that it would be a propertie from elemente, not just the element itself
def binary_search(nums, target):
    if len(nums) == 1:
        return nums[0] if nums[0] == target else None
    else:
        index = (len(nums) - 1) // 2
        guess = nums[index]
        # print(target, index, guess, nums)
        if guess == target:
            return guess
        if guess > target:
            return binary_search(nums[0:index-1], target)
        if guess < target:
            return binary_search(nums[index+1:], target)



# print(
#     suma(nums.copy())
# )

# print(
#     cardinality(nums.copy())
# )

# print(
#     maximum(nums.copy())
# )


print(
    binary_search(
        [
            1,2,4,5,6,
            7,8,9,12,24,
            45,56,67,88,89,
            90
        ], # 16 items
        50
    )
)