

def find_similariry(target, test):

    table = [ [ 0 for j in range(len(test) + 1)] for i in range(len(target) + 1) ]

    similarity = 0
    for i in range(1, len(target) + 1):
        for j in range(1, len(test) + 1):
            if target[i-1] == test[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                similarity = max(similarity, table[i][j])

    for row in table:
        print(row)

    return similarity


target = "hish"

# print(find_similariry(target, "fish"))

# print(find_similariry(target, "vista"))

def find_subsequence(target, test):

    table = [ [ 0 for j in range(len(test) + 1)] for i in range(len(target) + 1) ]

    for i in range(1, len(target) + 1):
        for j in range(1, len(test) + 1):
            if target[i-1] == test[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                upper_item = table[i-1][j]
                left_item = table[i][j-1]
                table[i][j] = max(upper_item, left_item)

    for row in table:
        print(row)

    return table[-1][-1]

print("fosh fish")
print(find_subsequence("fosh", "fish"))

print("fosh fort")
print(find_subsequence("fosh", "fort"))