

def max_substring_lenght(original: str):
    max_lenght = 0
    if len(original) == 0:
        return max_lenght
    
    last_index = len(original) - 1
    left_index = 0
    right_index = left_index

    while left_index <= last_index:
        characters = {}
        while right_index <= last_index:
            if original[right_index] in characters:
                break

            characters[original[right_index]] = True
            right_index += 1

        max_lenght = max(len(characters), max_lenght)
        left_index += 1
        right_index = left_index

    return max_lenght


print(
    max_substring_lenght("avaa")
)