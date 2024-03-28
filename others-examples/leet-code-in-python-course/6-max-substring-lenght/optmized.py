def max_substring_lenght(original: str):
    max_lenght = 0
    if len(original) == 0:
        return max_lenght
    
    # the dict will hold all found character matched with their last positions
    characters_seen = {}
    left_index = 0
    right_index = 0

    while left_index < len(original) and right_index < len(original):
        current_character = original[right_index]
        if current_character in characters_seen:
            previous_character_position = characters_seen[current_character]
            left_index = max(left_index, previous_character_position + 1)

        characters_seen[current_character] = right_index
        # after each interaction max_lenght could be updated, always to up.
        max_lenght = max(max_lenght, right_index - left_index + 1)
        # after each iteration R is incremented.
        print(left_index, right_index, characters_seen)
        right_index += 1

    return max_lenght


# area example
# 0 0 {'a': 0}
# 0 1 {'a': 0, 'e': 1}
# 0 2 {'a': 0, 'e': 1, 'r': 2}
# 1 3 {'a': 3, 'e': 1, 'r': 2}
print(
    max_substring_lenght("aera")
)