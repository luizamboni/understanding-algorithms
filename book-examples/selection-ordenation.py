
def selectSmaller(nums):
    min_index = 0

    for i in range(1, len(nums)):

        if nums[i] < nums[min_index]:
            min_index = i

    
    return min_index


def sortBySelection(nums):
    sortedList = []
    for i in range(len(nums)):
        smaller_index = selectSmaller(nums)
        sortedList.append(nums.pop(smaller_index))

    return sortedList

list1 = [54,5,2,1,5,2,10]



print(
    selectSmaller(list1)
)

print(
    sortBySelection(list1)
)