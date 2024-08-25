
def sumBinaries(a: str, b: str):

    
    a_pointer = len(a) - 1
    b_pointer = len(b) - 1
    carry = 0

    result = ""
    
    while (a_pointer >= 0 or b_pointer >= 0 or carry > 0):
        stack = carry
        if a_pointer >= 0:
            stack += int(a[a_pointer])
            a_pointer-= 1
            
        if b_pointer >= 0:
            stack += int(b[b_pointer])
            b_pointer-= 1

        
        result = str(stack % 2) + result
        carry = stack // 2

    return result






print(
    sumBinaries(
        "1011",
        "1101"
    )
)