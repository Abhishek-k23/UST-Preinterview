from collections import Counter

def word_frequency(line):
    words = line.lower().split()

    # Count & Sortthe words
    word_count = Counter(words)
    sorted_word_count = sorted(word_count.items())

    # Print in the desired format
    for word, count in sorted_word_count:
        print(f"('{word}', {count})")

if __name__ == "__main__":
    line = "which is better python 2 or python 3"
    word_frequency(line)
