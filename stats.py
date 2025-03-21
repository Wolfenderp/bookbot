def get_num_words(text):
    word_list = text.split()
    return len(word_list)
    
def get_num_characters(text):
    lower_case_text = text.lower()
    character_list = {}
    for char in lower_case_text:
        if char in character_list:
            character_list[char] += 1
        else:
            character_list[char] = 1
    return character_list

def sort_on(dict):
    return dict["count"]

def characters_list_sorting(character_list):
    char_list = []
    for char, count in character_list.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list