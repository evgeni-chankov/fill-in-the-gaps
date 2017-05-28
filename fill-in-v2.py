import game_data

def get_user_name():
    """ Gets user name """
    user_name = raw_input ("Hi, welcome to the quiz. What's your name? ")
    return user_name

def get_selected_difficulty(user_name):
    """ Greets user and prompts difficulty select """
    user_difficulty_selection = raw_input ("Hi %s, please select a difficulty (easy, medium, hard):" % (user_name)).lower()
    return user_difficulty_selection

def load_selected_difficulty(selected_difficulty,max_allowed_tries):
    """ Loads the corresponding text, based on user selection""" 
    if selected_difficulty == "easy":
        return play_mode('easy', game_data.game_data['easy']['quiz'], game_data.game_data['easy']['answers'], max_allowed_tries)
    elif selected_difficulty == "medium":
        return play_mode('medium', game_data.game_data['medium']['quiz'], game_data.game_data['medium']['answers'], max_allowed_tries)
    elif selected_difficulty == "hard":
        return play_mode('hard', game_data.game_data['hard']['quiz'], game_data.game_data['hard']['answers'], max_allowed_tries)
    else:
        print "Invalid selection"
        return play_game()

def inform_user(wrongs,max_wrongs_allowed,difficulty,current_hole,current_text):
    """ Informs user of position and conditions in current game """
    print "-" * 50
    print "Selected game conditions: "
    print "Maximum allowed wrong guesses: " + str(max_wrongs_allowed)
    print "Current number of wrong guesses: "+ str(wrongs)
    print "Here is the text for level " + difficulty + ": "
    print "-" * 50
    print current_text 
    print "-" * 50
    user_guess = raw_input("Your guess for hole " + current_hole + " :\n")
    return user_guess

def get_max_tries():
    """ Get user input to determine max number of wrong tries before game resets """
    max_tries = int(raw_input("What is the maximum number of wrong tries before the game resets? \n"))
    return max_tries

def play_mode(difficulty, level_text, answers, max_allowed_tries):
    """ Plays a full game in selected mode """ 
    counter, wrongs = 0, 0
    while counter < len(game_data.placeholders) and wrongs < max_allowed_tries:
        current_hole = game_data.placeholders[counter]
        correct_answer = answers[counter]
        user_guess = inform_user(wrongs, max_allowed_tries, difficulty, current_hole, level_text)
        if user_guess == correct_answer:
            correct_answer = answers[counter]
            level_text = level_text.replace(current_hole, correct_answer)
            print "Correct!"
            counter += 1
        else:
            print "Wrong"
            wrongs += 1
    if wrongs >= max_allowed_tries:
        print "Maximum number of tries reached! Please try again."
    return play_again()

def play_again():
    """ Allows user to restart a game after completing or getting kicked out. """
    another_try = raw_input("Would you like to play again? 'Y' for Yes or 'N' for No: \n").upper()
    if another_try == "Y":
        return play_game()
    else:
        print "Bye Bye!"

def play_game():
    """ This is the main method starting a game"""
    user_name = get_user_name()
    selected_difficulty = get_selected_difficulty(user_name)
    number_of_tries = get_max_tries()
    load_selected_difficulty(selected_difficulty,number_of_tries)

play_game()