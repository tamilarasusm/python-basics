def longest_substring_without_repeating_char(str):
    left = 0
    char_map = dict()
    max_value = 0
    for index, item in enumerate(str):
        if item in char_map:
            left = max(left, char_map.get(item) + 1)
            char_map[item] = index
        else:
            char_map[item] = index
            
        current_width = index - left + 1
        if(current_width > max_value ):
            max_value = current_width
            
    return max_value


print(longest_substring_without_repeating_char("abcabaa"))