# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.
glossary = {
    'comment': 'A comment allows you to write notes in English within your programs.',
    'list': 'Lists allow you to store sets of information in one place.',
    'loop': 'Looping allows you to take the same action, or set of actions,with every item in a list.',
    'indentation': 'Indentation is to determine how a line, or group of lines, is related to the rest of the program.',
    'python': 'programming language  which allows you to write programs.'}
for word, meaning in glossary.items():
    print(word.title(), ':', meaning)
