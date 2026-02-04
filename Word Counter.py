
# A WORD COUNTING PROGRAM USING PYTHON

def word_counter(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
        return None
    
filename = input("Enter the name of the file: ")
word_count = word_counter(filename)
if word_count is not None:
    print(f"The file '{filename}' contains {word_count} words.")
