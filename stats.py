def count_words(text:str):
    words_list = text.split()
    return len(words_list)


def count_characters(text:str):
    counts = {}
    for char in text:
        if char.lower() in counts:
            counts[char.lower()] += 1
        else:
            counts[char.lower()] = 1
    return counts

def get_value(t):
    return t[1]


def sort_charcter_count(char_dict: dict):
    sorted_all_char_dict = { k: v for k, v in sorted(char_dict.items(), key=get_value, reverse=True)}
    sorted_alpha_char_dict = {}
    for k in sorted_all_char_dict:
        if k.isalpha():
            sorted_alpha_char_dict[k] = sorted_all_char_dict[k]   
    return sorted_alpha_char_dict