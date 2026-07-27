def count_spaces(text):
    count = 0

    for ch in text:
        if ch == " ":
            count += 1

    return count

sentence = input("Enter a sentence: ")

print("Number of spaces =", count_spaces(sentence))