def ask_for_info():
    question = """/n
    Which of the following food choices do you prefer?
         A. Spaghetti
         B. Bratwurst
         C. Lomein
         D. Falafel/n : """
    food_preference = (raw_input(question)).upper()

    if food_preference == "A":
        print "Let's go to Italy!"
    elif food_preference == "B":
        print "Let's go to Germany!"
    elif food_preference == "C":
        print "Let's go to China!"
    elif food_preference == "D":
        print "Let's go to Israel!"

    next_question = (raw_input("Do you want to specify where to go? ")).lower()

    if next_question == "yes":
        specify_region()
    elif next_question == "no":
        print "Goodbye!"
    else:
        print "Please give a yes or no answer."

def specify_region():
    remind_of_country = (raw_input("Which country are you going to? ")).capitalize()

    if remind_of_country == "Italy":
        within_Italy()
    elif remind_of_country == "Germany":
        within_Germany()
    elif remind_of_country == "China":
        within_China()
    elif remind_of_country == "Israel":
        within_Israel()
    else:
        print "Please choose a country that is on our list. "
# ----------------------------------------------------------------

ask_for_info()