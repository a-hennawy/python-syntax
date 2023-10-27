def print_upper_words(word_list):
    """Takes in a list of words, capitalizes them and prints them on separate lines"""
    for word in word_list:
        print(word.upper())


def print_upper_words2(word_list):
    """Takes in a list of words, capitalizes words starting with an 'e' and prints them on separate lines"""
    for word in word_list:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words3(word_list, starts_with):
    """Takes in a list of words, capitalizes words starting with an 'e' and prints them on separate lines"""
    for word in word_list:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())


# print_upper_words(["apple", "hi", "hello"])
# print_upper_words2(["apple", "hi", "hello", "ears"])
print_upper_words3(["apple", "hi", "hello", "ears", "yes"], ["h", "y"])
