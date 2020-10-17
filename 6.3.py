# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
glossary = {
    'comment': 'A comment allows you to write notes in English within your programs.',
    'list': 'Lists allow you to store sets of information in one place.',
    'loop': 'Looping allows you to take the same action, or set of actions,with every item in a list.',
    'indentation': 'Indentation is to determine how a line, or group of lines, is related to the rest of the program.',
    'python': 'programming language  which allows you to write programs.'}
print('comment'.title(),':')
print(glossary['comment'])
print('list'.title(),':')
print(glossary['list'])
print('loop'.title(),':')
print(glossary['loop'])
print('indentation'.title(),':')
print(glossary['indentation'])
print('python'.title(),':')
print(glossary['python'])
