def read_swears_from_file(file_path):
    with open(file_path, 'r') as file:
        swear_words = [line.strip() for line in file]
    return swear_words

def detoxify_text(text, swear_words):
    words = text.split()
    cleaned_words = []
    for word in words:
        lower_word = word.lower()
        if lower_word not in swear_words:
            cleaned_words.append(word)
        else:
            cleaned_words.append("*" * len(word))  # Replace the word with asterisks of the same length
    cleaned_text = ' '.join(cleaned_words)
    return cleaned_text

def main():
    file_path = "swearwords.txt"  # Path to the text file containing the swear words
    swear_words = read_swears_from_file(file_path)

    user_input = input("Enter some text: ")
    detoxified_text = detoxify_text(user_input, swear_words)
    print("Detoxified Text: ", detoxified_text)

if __name__ == "__main__":
    main()
