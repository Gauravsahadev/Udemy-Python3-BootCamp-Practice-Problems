def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

print(multiple_letter_count("gaurav"))