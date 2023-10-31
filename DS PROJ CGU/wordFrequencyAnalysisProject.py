from collections import Counter
import string

print("Welcome to the Word Frequency Analysis App")

# Function to clean and tokenize text
def clean_and_tokenize(text):
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    return words

# Read text from a file
file_name = input("Please enter the path to a text document file: ")
try:
    with open(file_name, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    exit()

words = clean_and_tokenize(text)

# Perform word frequency analysis
word_count = Counter(words)

# Writing the word frequency analysis to an output file
output_file = "word_frequency_analysis_output.txt"
with open(output_file, 'w') as output:
    output.write("Word Frequency Analysis\n")
    output.write("Word\t\tOccurrence Frequency\n")
    for word, frequency in word_count.items():
        output.write(f"{word}\t\t{frequency}\t\t{frequency / len(words) * 100:.2f}%\n")

    most_common_words = word_count.most_common(10)  # Change 10 to the desired number of most common words
    output.write("\nMost Common Words:\n")
    for word, frequency in most_common_words:
        output.write(f"{word}: {frequency} times\n")

print(f"Word frequency analysis has been saved to '{output_file}'")
