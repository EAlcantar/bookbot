def number_of_words(text):
    num_words = len(text.split())
    words = text.split()
    print(f"Found {num_words} total words")
    return

def character_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters_by_count(char_count):
    sorted_characters = [{'character': char, 'count': count} for char, count in char_count.items()]
    sorted_characters.sort(key=lambda x: x['count'], reverse=True)
    return sorted_characters