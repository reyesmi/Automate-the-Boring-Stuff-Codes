# English to Pig Latin - Pig Latin is a silly made-up language that alters English words.
    # If a word begins with a vowel, the word yay is added to the end of it.
    # If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay.
""" First, we ask the user to enter English text to translate into Pig Latin.
We then create a constant that holds every lowercase vowel letter (and y) as a tuple of strings.
"""
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u','y')
""" Next, we're going to create the pigLatin variable to store the words as we translate them into Pig Latin. """
pigLatin = [] # A list of the words in Pig Latin.
""" Separate the non letters from the start and end of the word. """
for word in message.split(): # We need each word to be its own string, so we call message.split()
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0] # Save the non-letters to a variable named prefixNonLetters
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1] # Save the non letters into a variable named suffixNonLetters
        word = word[:-1]

    # Remember if the word was in uppercase or title case, so that we can restore it after translating to pig Latin.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation
# To convert a word starting with consonants (or consonant clusters), we need to remove those consonant/consonant clusters from the beginning of the word. 
    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0] # Save the consonants in a variable named prefixConsonants
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(''.join(pigLatin))
