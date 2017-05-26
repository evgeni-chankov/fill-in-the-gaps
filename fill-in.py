""" The data for the easy level """
placeholders = ['__1__','__2__','__3__','__4__','__5__']

easy_text = """
Pirates of the Caribbean is a __1__ media franchise encompassing numerous theme park attractions, 
a series of films, and spin-off novels, as well as a number of related video games and other media publications. 
The franchise originated with the Pirates of the Caribbean theme ride attraction, which opened at __2__ in 
1967 and was one of the last Disney theme park attractions overseen by __3__. Disney based the ride on pirate 
legends and folklore. As of October 2016, Pirates of the Caribbean attractions can be found at __4__ Disney theme parks. 
Their related films have grossed over US$ 3.7 billion worldwide as of January 2015, putting the film franchise __5__ in
the list of all-time highest grossing franchises and film series. 

"""
easy_text_answers = ["Disney", "Disneyland", "Walt Disney", "five", "11th"]

def get_user_name():
    """ Gets user name """
    user_name = raw_input ("Hi, welcome to the quiz. What's your name? ")
    return user_name

def get_selected_difficulty(user_name):
    """ Greets user and prompts difficulty select """
    user_difficulty_selection = raw_input ("Hi %s, please select a difficulty (easy, medium, hard):" % (user_name)).lower()
    return user_difficulty_selection

def load_selected_difficulty(selected_difficulty):
    """ Loads the corresponding text, based on user selection""" 
    if selected_difficulty == "easy":
        return play_easy()
    elif selected_difficulty == "medium":
        print "hiya medium"
    elif selected_difficulty == "hard":
        print "hiya hard"
    else:
        print "Invalid selection"
        return play_game()

def play_easy():
    """ Plays a full game in easy mode """ 
    counter = 0
    max_wrongs_wanted = int(raw_input("What is the maximum number of wrong tries before the game resets? \n "))
    wrongs = 0
    replaced = easy_text
    while counter < 5 and wrongs < max_wrongs_wanted:
        print "Current counter position is: " + str(counter)
        current_hole = placeholders[counter]
        print "Current hole is: "+current_hole
        correct_answer = easy_text_answers[counter]
        print "Correct answer is: "+correct_answer
        print "Maximum nr of wrongs wanted: " + str(max_wrongs_wanted)
        print "Number of wrong tries: "+ str(wrongs)
        print "-" * 50 + "\n Here is the text for level easy: "
        print replaced 
        user_guess = raw_input("Your guess for hole " + current_hole + " :\n")
        if user_guess == correct_answer:
            correct_answer = easy_text_answers[counter]
            replaced = replaced.replace(current_hole, correct_answer)
            print replaced
            counter += 1
            print "Correct!"
        else:
            print "Wrong"
            wrongs += 1
    if wrongs >= max_wrongs_wanted:
        print "Maximum number of tries exceeded!"

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
    load_selected_difficulty(selected_difficulty)

play_game()