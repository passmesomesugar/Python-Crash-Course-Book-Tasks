# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
favorite_languages_poll_list = {'bjarne', 'linus', 'turing', 'rossum', 'Ritchie'}
favorite_languages = {
    'bjarne': 'c++',
    'jen': 'python',
    'linus': 'c',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for poll_takers in favorite_languages_poll_list:
    if poll_takers in favorite_languages.keys():
        print("Thank you for response", poll_takers.title())
    else:
        print("Please take a poll", poll_takers.title())
