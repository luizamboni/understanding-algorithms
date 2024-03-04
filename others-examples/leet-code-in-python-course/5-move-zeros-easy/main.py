from time import sleep

def my_solution(nums):
    lindex = 0
    rindex = len(nums) - 1 
    while lindex < rindex:
        sleep(0.5)

        if nums[lindex] == 0:
            rindex -= 1
            nums.append(nums[lindex])
            del nums[lindex]
        lindex += 1
    
    return nums

def course_solution(nums):
    lindex = 0
    rindex = len(nums) - 1
    zero_index_track = 0

    while zero_index_track <= rindex:
        if nums[zero_index_track] != 0:
            print("non_zero_index", zero_index_track)
            nums[lindex] = nums[zero_index_track]
            lindex += 1
        zero_index_track += 1

    for i in range(lindex, rindex+1):
        nums[i] = 0

    return nums



print("result:", my_solution([ 0, 1, 0, 3, 12]))
print("result:", course_solution([ 0, 1, 0, 3, 12]))

print("result:", my_solution([ 0, 1, 0, 3,0, 1]))
print("result:", course_solution([ 0, 1, 0, 3,0, 1]))