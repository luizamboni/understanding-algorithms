

def find_min_window(s, t):
    marks = []
    for i in range(len(s)):
        for j in t:
            if j == s[i]:
                marks.append((i, s[i]))
    
    print(marks)
    canditate = (0,0)
    for i in range(len(t) - 1, len(marks) -1):
        window = marks[i - (len(t) - 1):i+1]
        if len(set(list(map(lambda x: x[1], window)))) == len(window):

            canditate = (window[0][0], window[len(window) - 1][0]) 

    return s[canditate[0]:canditate[1]+1]


examples = [
    { "s": "ADOBECODEBANCC", "t": "ABC" },
    { "s": "asdhnsshadeeweq", "t": "shade" },
    { "s": "asshnashcjhdeweq", "t": "shade" }, # fails here
]
for example in examples:

    print(
        find_min_window(example["s"], example["t"])
    )