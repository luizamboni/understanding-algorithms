nums = [ 2, 1, 3, 1, 1 ]

def find_majority(nums):
    lenght = len(nums)
    m = {}
    for i in range(lenght):
        if nums[i] in m:
            m[nums[i]] += 1
        else:
            m[nums[i]] = 1

        if m[nums[i]] >= int(lenght/2) + 1:
            return nums[i]
        
print(
    find_majority(nums)
)