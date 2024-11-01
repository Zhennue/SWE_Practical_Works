def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

# Test the function
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")


from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def find_longest_word(content):
    words = content.split()
    longest_word = max(words, key=len)
    return longest_word

# Test the function
longest_word = find_longest_word(content)
print(f"Longest word: '{longest_word}'")

def word_occurrences(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())

# Test the function
target_word = 'example'  # Change to any word you'd like to search for
occurrences = word_occurrences(content, target_word)
print(f"The word '{target_word}' appears {occurrences} times")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_than_avg = [word for word in words if len(word) > avg_length]
    return (len(longer_than_avg) / len(words)) * 100

# Test the function
percentage_longer = percentage_longer_than_average(content)
print(f"Percentage of words longer than average length: {percentage_longer:.2f}%")