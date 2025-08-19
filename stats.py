

def count_words(text):
    num_words = text.split()
    return len(num_words)

def count_chars(text):
    char_count = {}
    ltext = text.lower()
    for char in ltext:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_list(dict_chars):
    list_of_dicts = [{"char" : k,"num":v} for k,v in dict_chars.items()]
    sorted_list = sorted(list_of_dicts, reverse=True, key=sort_on)
    return sorted_list
