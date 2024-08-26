nums = [ 2, 1, 3, 1, 1 ]

def find_majority(nums):
    lenght = len(nums)
    for i in range(lenght):
        count = 1
        for j in range(lenght):
            if j == i:
                continue
        
            if nums[i] == nums[j]:
                count += 1
        
        if count >= int(lenght/2) + 1:
            return nums[i]
        
print(
    find_majority(nums)
)