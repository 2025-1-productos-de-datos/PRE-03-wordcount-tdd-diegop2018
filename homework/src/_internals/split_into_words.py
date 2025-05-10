def split_into_words(preprocess_lines):
    words = []
    for line in preprocess_lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words
