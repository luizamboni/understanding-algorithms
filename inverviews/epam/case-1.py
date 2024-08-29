
def calc_moves(nums):
    incr = 0
    moves = 0

    for i in range(1, len(nums)):
        curr=nums[i]
        prev=nums[i-1]
        if prev + incr >= curr + incr:
            incr = (prev + incr) - (curr) + 1
            moves+=1
        # print(incr)

    return moves

input1=[4,2,4,1,3,5]
input2=[3,5, 7,7]
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

