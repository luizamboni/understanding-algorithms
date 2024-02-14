nums = [1,7,3,5,4,6,2,8]
# nums = [1,2,3,4,5,6,7,8] # sorted list

def quicksort(nums):
    print("quicksort")

    if len(nums) < 2:
        return nums
    
    pivot = nums[0]
    smaller = [ n for n in nums[1:] if n <= pivot ]
    higher  = [ n for n in nums[1:] if n > pivot  ]

    return quicksort(smaller) + [pivot] + quicksort(higher)



print(
    quicksort(nums)
)


def quicksort2(nums):
    print("quicksort2")
    if len(nums) < 2:
        return nums
    
    pivot_index = (len(nums) - 1) // 2
    pivot = nums[pivot_index]
    smaller = [ n for n in nums[0:pivot_index] + nums[pivot_index+1:] if n <= pivot]
    higher  = [ n for n in nums[0:pivot_index] + nums[pivot_index+1:] if n > pivot ]

    return quicksort2(smaller) + [pivot] + quicksort2(higher)


print(
    quicksort2(nums)
)
