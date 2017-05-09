def greet_user():
    print "Welcome to Follow Your Tastes."
    print "We look forward to seeing where you will go!"

def ask_for_info():
    question = """
    Which of the following food choices do you prefer?
         A. Spaghetti
         B. Bratwurst
         C. Lomein
         D. Falafel : """/n
    food_preference = (raw_input(question)).upper()

    return food_preference

def creates_prints_destination(food_preference):

    if food_preference == "A":
        print "Let's go to Italy!"
    elif food_preference == "B":
        print "Let's go to Germany!"
    elif food_preference == "C":
        print "Let's go to China!"
    elif food_preference == "D":
        print "Let's go to Israel!"

def ask_if_continue_to_region():
    next_question = (raw_input("Do you want to go to a specific region? ")).lower()

    if next_question == "yes":
        country = (raw_input("Which country are you going to?")).capitalize()
        specify_region(country)
    elif next_question == "no":
        print "Goodbye!"
    else:
        print "Please give a yes or no answer."

def specify_region(country):
    if country == "Italy":
        within_Italy()
    elif country == "Germany":
        within_Germany()
    elif country == "China":
        within_China()
    elif country == "Israel":
        within_Israel()
    else:
        print "Please choose a country that is on our list. "

def ask_if_repeat_whole_process():
# --------------------------------------------------------------

greet_user()
playing = True
while playing:
    ask_for_info() = food_preference
    creates_prints_destination(food_preference)
    ask_if_continue_to_region()
    ask_if_repeat_whole_process()