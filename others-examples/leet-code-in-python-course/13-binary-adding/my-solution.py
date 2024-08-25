
def sumBinaries(a: str, b: str):

    
    carry = False

    sum = ""
    for i in range(len(a) -1 , -1, -1):
        if a[i] != b[i]:
            if carry:
                sum = "0" + sum
            else:
                sum = "1" + sum
                carry = False
        elif a[i] == "0" and b[i] == "0":
            if carry:
                sum = "1" + sum
            else:
                sum = "0" + sum
            carry = False
        else:
            if carry:
                sum = "1" + sum
            else:
                sum = "0" + sum
            carry = True

    if carry:
        sum = "1" + sum

    return sum


print(
    sumBinaries(
        "1111",
        "1101"
    )
)