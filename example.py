import json

numbers = [2, 3, 5, 7, 11, 14]
filename = 'Do It Yourself section tasks/Chapter 10/numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

