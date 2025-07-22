def word_counter(test_file):
    try:
        with open(test_file) as file:
            inside = file.read()
            words = inside.split()
            word = len(words)
            return word
    except FileNotFoundError:
        return f"Error : the file '{test_file}'was not found"
    except Exception as e:
        return f"An error occurred: {e}"


file_path = r"C:\Users\DELL\OneDrive\Desktop\Word counter\test_file.txt"
total_words = word_counter(file_path)
print("---------------program start---------------\n")
if isinstance(total_words, int):
    print(f"Total number of words in '{file_path}': {total_words}")
else:
    print(total_words)
print("\n---------------program end---------------")
