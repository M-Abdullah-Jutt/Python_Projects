
# # Word Counter
text = input('Enter Your Sentence: ')
words = text.split()
words_length = len(words)

print(f'Total Number of Words are {words_length}')


# Words + Character Counter using 'collections' library
from collections import Counter

# words counter
text = input('Enter Your Sentence: ')
words = text.split()
words_counter = Counter(words)
print('Word counts...')
for word, count in words_counter.items():
    print(f'{word},{count}')

# characters counter
char_counts = Counter(text)
print('\nCharacter counts...')
for char, count in char_counts.items():
    print(f'{char},{count}')