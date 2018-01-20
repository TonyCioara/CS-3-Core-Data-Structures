#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    pattern_index = 0
    text_index = 0
    while text_index < len(text):
        if pattern_index > len(pattern) - 1:
            return True
        if pattern[pattern_index] == text[text_index]:
            if pattern_index == len(pattern) - 1:
                return True
            pattern_index += 1
        elif pattern_index != 0:
            text_index -= pattern_index
            pattern_index = 0
        text_index += 1
    return False


def find_index(text, pattern, pattern_index=0, text_index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern == "":
        return 0
    if (pattern_index == len(pattern)):
        return text_index - len(pattern)
    if (text_index == len(text)):
        return None
    if text[text_index] == pattern[pattern_index]:
        return find_index(text, pattern, pattern_index + 1, text_index + 1)
    if pattern_index == 0:
        return find_index(text, pattern, 0, text_index + 1)
    else:
        return find_index(text, pattern, 0, text_index - pattern_index + 1)


def find_all_indexes(text, pattern, pattern_index=0, text_index=0, index_array=None):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    if index_array is None:
        index_array = []
    if pattern == "":
        if text_index >= len(text):
            return index_array
        index_array.append(text_index - len(pattern))
        return find_all_indexes(text, pattern, 0, text_index + 1, index_array)
    if pattern_index >= len(pattern):
        index_array.append(text_index - len(pattern))
        next_text_index = text_index - len(pattern) + 1
        return find_all_indexes(text, pattern, 0, next_text_index, index_array)
    if text_index >= len(text):
        return index_array
    if text[text_index] == pattern[pattern_index]:
        return find_all_indexes(text, pattern, pattern_index + 1, text_index + 1, index_array)
    if pattern_index == 0:
        return find_all_indexes(text, pattern, 0, text_index + 1, index_array)
    else:
        return find_all_indexes(text, pattern, 0, text_index, index_array)

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    print(find_all_indexes('abc', 'z'))
    find_all_indexes('abc', 'a') == [0]  # single letters are easy
    find_all_indexes('abc', 'b') == [1]
    find_all_indexes('abc', 'c') == [2]
    print('should all be empty:')
    find_all_indexes('abc', 'z') == []  # remember to test other letters
    find_all_indexes('abc', 'ac') == []  # important to test close cases
