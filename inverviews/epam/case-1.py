
def calc_moves(nums):
    incr = 0
    l = 1
    l2 = 1
    moves = 0
    r = len(nums) - 1

    while l2 <= r:
        print("-> comparing", nums[l2-1] , nums[l2] )
        if nums[l2] + incr <= nums[l2-1]:
            incr = nums[l2-1] - nums[l2] + 1
            moves+=1
        else:
            # apply the increment to prev elements
            for j in range(l, l2+1):
                nums[j]=nums[j]+incr
            l=l2+1
        l2+=1


    print(nums)
    return moves

input1=[4,2,4,1,3,5]
input2=[3,5,7,7]
input3=[1,5,6,10] 

print(
    calc_moves(input1)
)

print(
    calc_moves(input2)
)

print(
    calc_moves(input3)
)

