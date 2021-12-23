input = "abacabade"


def find_not_repeating_character(string):

    occurrence_alphabet = [0] * 26

    for char in string:
        occurrence_index = ord(char) - ord('a')
        occurrence_alphabet[occurrence_index] += 1

    not_repeating_character_list = []

    for i, char in enumerate(occurrence_alphabet):
        if char == 1:
            not_repeating_character_list.append(chr(i + ord('a')))

    print(not_repeating_character_list)

    for compare in string:
        if len(not_repeating_character_list) == 0:
            return '-'
        elif compare in not_repeating_character_list:
            return compare
    return 0


result = find_not_repeating_character(input)
print(result)