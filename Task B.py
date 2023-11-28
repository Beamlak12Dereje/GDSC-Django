def calculate_word_lengths(word_list = input("Enter word list: ")):
    word_lengths = [len(word) for word in word_list]
    return word_lengths
def average_word_length(word_lengths):
    return sum(word_lengths) / len(word_lengths)

def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word, len(longest_word)
    print(longest_word, len(longest_word))

def find_shortest_word(word_list):
    shortest_word = min(word_list, key=len)
    return shortest_word, len(shortest_word)
def word_length_distribution(word_list = input("enter the word: ")):
    word_length_freq = {}
    for word in word_list:
        length = len(word)
        if length in word_length_freq:
            word_length_freq[length] += 1
        else:
            word_length_freq[length] = 1
    return word_length_freq
def display_word_length_distribution(word_length_freq):
    sorted_word_length_freq = dict(sorted(word_length_freq.items()))
    for length, freq in sorted_word_length_freq.items():
        print(f"Word length {length}: {freq}")
display_word_length_distribution(word_length_distribution(word_list = input("enter the word: ")))