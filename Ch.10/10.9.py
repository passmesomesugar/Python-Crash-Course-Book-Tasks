# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.
def read_contents(source_file):
    """Count the approximate number of words in a file."""
    try:
        with open(source_file, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"{source_file} contents:\n{contents}")


filename = "dogs.txt"
read_contents(filename)

filename = "cats.txt"
read_contents(filename)

filename = "non-existent.txt"
read_contents(filename)
