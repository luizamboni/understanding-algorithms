from typing import List

examples = [  
        # moves   3   5   7   7
        # surpus -3   2   2   0
    {   # diff   -3   5   0  -2
        "input": [7, 15, 10, 8],
        "expected": 7,
    },
    {
        # moves    1  2   3  4   5   6   6
        # suplus   1  1  -1  1  -1  -1   0
        # diff     1  0  -2  2  -2   0   1
        "input": [11, 10, 8, 12, 8, 10, 11],
        "expected": 6,
    },
    {
        # moves     3  4   5
        # surplus  -3  1   1
        # diff     -3  4   0
        "input":  [ 7, 14, 10],
        "expected": -1,
    },
]

#GPT solution
def calculate_movies(A):
    target = 10
    N = len(A)
    
    moves = 0
    surplus = 0
    
    for i in range(N):
        surplus += A[i] - target
        moves += abs(surplus)
        # print(f"{A[i]}\t{A[i] - target}\t{surplus},\t{moves}")
    
    if surplus != 0:
        return -1

    return moves

for example in examples:
    print(
        calculate_movies(example["input"])
    )