# This string will only contain a single word,
# but there is no guarantee whether the word will be upper case,
# lower case, mixed case, or have leading / trailing spaces or
# punctuation.

def main():
    tach_status = is_tachycardic()

def is_tachycardic():
    word_input = input("Please enter word: ")
    word = word_input.lower()
    tach_status = 'tachycardic' in word
    print("The answer is {}".format(tach_status))
    return tach_status

if __name__ == "__main__":
	main()
