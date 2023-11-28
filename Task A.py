def get_input_text():
    input_text = input("Enter a paragraph of text: ")
    return input_text
def tokenize_text(input_text):
    word_list = input_text.split()
    return word_list
def calculate_word_frequencies(word_list):
    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq
def display_word_frequencies(word_freq):
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    for word, freq in sorted_word_freq.items():
        print(f"{word}: {freq}")
display_word_frequencies(calculate_word_frequencies(tokenize_text(get_input_text())))
def display_top_n_words(word_freq, n = input(("Enter the value of n"))):
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    top_n_words = list(sorted_word_freq.items())[:n]
    for word, freq in top_n_words:
        print(f"{word}: {freq}")
display_top_n_words(display_word_frequencies(calculate_word_frequencies(tokenize_text(get_input_text()))))
def search_word_frequency(word_freq, search_word):
    if search_word in word_freq:
        print(f"The frequency of '{search_word}' is {word_freq[search_word]}")
    else:
        print(f"The word '{search_word}' is not found in the text.")
def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word

def calculate_average_word_length(word_list):
    total_length = sum(len(word) for word in word_list)
    average_length = total_length / len(word_list)
    return average_length


