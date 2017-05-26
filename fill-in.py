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

medium_text = """
The unnamed Narrator (__1__) is a traveling automobile recall specialist who suffers from insomnia. 
When he is unsuccessful at receiving medical assistance for it, the admonishing doctor suggests he realize his 
relatively small amount of suffering by visiting a support group for __2__ cancer victims. The group assumes 
that he, too, is affected like they are, and he spontaneously weeps into the nurturing arms of another man, 
finding a freedom from the catharsis that relieves his insomnia. He decides to participate in support groups of various kinds, 
always allowing the groups to assume that he suffers what they do. However, he begins to notice another __3__, 
Marla Singer (__4__), whose presence reminds him that he is attending these groups dishonestly, 
and this disturbs his bliss. The two __5__ to avoid their attending the same groups, but, 
before going their separate ways, Marla gives him her phone number.

"""
medium_text_answers = ["Edward Norton", "testicular", "impostor", "Helena Bonham Carter", "negotiate"]

hard_text = """
Heat is a __1__ American crime film written, produced and directed by __2__, and starring Robert De Niro, 
Al Pacino, and __3__. De Niro plays Neil McCauley, a professional thief, while Pacino plays Lt. Vincent Hanna, 
a LAPD robbery-homicide detective tracking down McCauley's crew. The story is based on the former Chicago police officer 
__4__'s pursuit during the 1960s of a criminal named McCauley, after whom De Niro's character is named.
Heat is a remake by Mann of a TV series he had worked on, the pilot of which was released as a TV movie, __5__ in 1989.

"""
hard_text_answers = ["1995", "Michael Mann", "Val Kilmer", "Chuck Adamson", "L.A. Takedown"]


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
        return play_mode('easy', easy_text, easy_text_answers)
    elif selected_difficulty == "medium":
        return play_mode('medium', medium_text, medium_text_answers)
    elif selected_difficulty == "hard":
        return play_mode('hard', hard_text, hard_text_answers)
    else:
        print "Invalid selection"
        return play_game()

def play_mode(difficulty, level_text, answers):
    """ Plays a full game in easy mode """ 
    counter = 0
    max_wrongs_wanted = int(raw_input("What is the maximum number of wrong tries before the game resets? \n "))
    wrongs = 0
    replaced = level_text
    while counter < 5 and wrongs < max_wrongs_wanted:
        print "Current counter position is: " + str(counter)
        current_hole = placeholders[counter]
        print "Current hole is: "+current_hole
        correct_answer = answers[counter]
        print "Correct answer is: "+correct_answer
        print "Maximum nr of wrongs wanted: " + str(max_wrongs_wanted)
        print "Number of wrong tries: "+ str(wrongs)
        print "-" * 50 + "\n Here is the text for level" + difficulty + ": "
        print replaced 
        user_guess = raw_input("Your guess for hole " + current_hole + " :\n")
        if user_guess == correct_answer:
            correct_answer = answers[counter]
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