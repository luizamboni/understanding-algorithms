# endode and decode

# encode
# a4b3c2 => aaaabbbcc

# decode
# aaaabbbcc => a4b3c2


input1_encode = "aaaabbbcc"


def encode(input: str):
    
    ans = input[0]
    count = 1

    for i in range(1, len(input)):

        if input[i-1] == input[i]:
            count+=1
        else:
            ans+=str(count)
            ans+=input[i]
            count = 1

    ans+=str(count)

    return ans


# print(
#     encode(input1_encode)
# )

input1_decode = "a20b3c2"

def decode(input: str):
    ans = ""
    
    l = 1
    r = len(input) - 1

    while l < r:
        for i in range(l, r):
            if input[i] not in "0123456789":
                for _ in range(int(input[l: i])):
                    ans+=input[l-1]
                l+=i
        l+=1

    for _ in range(int(input[r])):
        ans+=input[r-1]

    return ans


print(
    decode(input1_decode)
)