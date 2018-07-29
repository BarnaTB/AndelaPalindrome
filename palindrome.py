def palindrome():
    """
    Function checks whether or not the user input would be the same when spelt
    backwards.
    """
    palindromes = []

    while True:
        the_word = raw_input("Please enter a word: ")
        word = the_word.lower()
        word = word.replace(' ', '')

        if word == 'quit':
            break
        if word.isalpha():
            if list(word) == list(reversed(word)):
                while(len(palindromes) > 4):
                    palindromes.pop(0)
                save_word = the_word + '\n'
                data = open('data.txt', 'a')
                data.write(save_word)
                data.close()

                print("{} is a palindrome".format(the_word))
                palindromes.append(the_word)
                print("Any other word? Type 'quit' if not.")

            else:
                print("{} is not a palindrome".format(the_word))
                print("Any other word? Type 'quit' if not.")
        else:
            print('Word should be a string without punctuation!')
    print('Your palindromes {}'.format(palindromes))

palindrome()
