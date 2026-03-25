def reverse_string(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')
