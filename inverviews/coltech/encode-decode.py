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


def decode(input: str):
    ans = ""
    
    char_index = 0
    count_r_index = 1
    r = len(input)

    for i in range(1, r):
        if input[i] in "0123456789":

            count_r_index+=1
        else:
            for _ in range(int(input[char_index+1: count_r_index])):
                ans+=input[char_index]
            char_index = i
            count_r_index = char_index + 1

    for _ in range(int(input[char_index+1: count_r_index])):
        ans+=input[char_index]
    return ans

input1_decode = "a20b3c10"

print(
    decode(input1_decode)
)
