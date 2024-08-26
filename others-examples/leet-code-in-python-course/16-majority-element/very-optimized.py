nums = [ 2, 1, 3, 1, 1 ]

def find_majority(nums):
    candidate = nums[0]
    votes = 1

    for current in nums[1:]:
        if votes == 0:
            candidate = current
            
        if current == candidate:
            votes += 1
        else:
            votes -= 1

    return candidate
        
print(
    find_majority(nums)
)