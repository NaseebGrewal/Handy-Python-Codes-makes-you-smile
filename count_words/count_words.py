import string


def remove_punctuation(input_text):
    # create a new string with all punctuation characters removed
    new_text = ""
    for char in input_text:
        if char not in string.punctuation:
            new_text += char

    return new_text


def count_words(input_text):
    # remove punctuation from input text
    input_text = remove_punctuation(input_text)

    # split input into words
    words = input_text.split()

    # count number of words
    num_words = len(words)

    return num_words


def main():
    # ask user for input method
    input_method = input("Enter 'T' to input text or 'F' to input a file path: ")

    # input_method = "how are you"

    # get input based on user's choice
    if input_method.upper() == "T":
        input_text = input("Enter your text: ")
    elif input_method.upper() == "F":
        file_path = input("Enter the file path: ")
        # open file and read contents
        with open(file_path, "r") as f:
            input_text = f.read()
    else:
        print("Invalid input method.")
        return

    # count number of words and print result
    num_words = count_words(input_text)
    print(f"The input contains {num_words} words.")


if __name__ == "__main__":
    main()

# print("python")
