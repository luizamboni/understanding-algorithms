input = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(input):
    ans = []
    m = {}

    for item in input:
        k = str(sorted(item))
        if k in m:
            m[k].append(item)
        else:
            m[k] = [item]
    
    for k in m:
        ans.append(m[k])

    return ans

print(
    group_anagrams(input)
)
        