import random



def read_file(file_name):
    with open(file_name, 'r') as some_words:
        some_words = open(file_name, 'r')
        words = some_words.readlines()
        return words


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word, words


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_index = random.randint(0, len(word)-1)
    random_letter = word[random_index]
    mylist = [i for i in word]
    # print(mylist)
    mylist1 = mylist
    # print(mylist1)
    for i in range(0,len(word)):
        mylist1[i] = "_"
    new_word = "".join(mylist1)
    # print(new_word)
    new_word2 = new_word[:random_index] + random_letter + new_word[random_index+1:]
    # print(new_word2)
    return new_word2, word


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    # index = 0

    # while index < len(answer_word) - 1:
    #     if char == original_word[index] and char != answer_word[index]:
    #         return True
    #     else:
    #         return False
    #     index += 1
    #     break

    # for i in range(len(answer_word)):
        if char in original_word and char not in answer_word:
            return True
        else:
            return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    #code to add the user character to the answer_word
    word_list = list(answer_word)
    word_index = len(original_word)-1
    start = 0
    while start < word_index:
        if original_word[start] == char:
            word_list[start] = char
            start += 1
        else:
            start += 1
    joined = "".join(word_list)
    return joined
    # index = original_word.find(char)
    # new_list = list(answer_word)
    # new_list[index] = char
    # new_word = "".join(new_list)
    # return new_word


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    number_guesses -= 1
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)
    return number_guesses


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
        if number_guesses == 4:
            print("/----\n|\n|\n|\n|\n_______")
        elif number_guesses == 3:
            print("/----\n|   0\n|\n|\n|\n_______")
        elif number_guesses == 2:
            print("/----\n|   0\n|  /|\\\n|\n|\n_______")
        elif number_guesses == 1:
            print("/----\n|   0\n|  /|\\\n|   |\n|\n_______")
        elif number_guesses == 0:
            print("/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______")
        print()

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed

# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`

# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    tries = 5
    while tries > 0:
        if answer == word:
            print("Correct!!!\nExit Game...")
            break
        else:
            guess = get_user_input()
            if guess == "exit" or guess == "quit" or guess == "q":
                print("Bye!")
                break
            elif is_missing_char(word, answer, guess):
                answer = do_correct_answer(word, answer, guess)
            else:
                tries -= 1
                do_wrong_answer(answer, tries)
    if tries == 0:
        print("Sorry, you are out of guesses. The word was: " + word)

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)
