def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    begin_i = 0
    end_i = len(text)
    if text.count(begin)>0:
        begin_i = text.index(begin)
        text = text.replace(begin,'')
    if text.count(end)>0:
        end_i = text.index(end)

    if (begin_i > end_i):
        end_i = begin_i

    print(text[begin_i:end_i])
    return text[begin_i:end_i]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
