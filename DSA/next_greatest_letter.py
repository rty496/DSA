def next_greatest_letter(letters, target):
    for ch in letters:
        if ch > target:
            return ch
    return letters[0]
