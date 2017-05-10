def greet_user():
    print "Welcome to Follow Your Tastes."
    print "We look forward to seeing where you will go!"

def ask_for_info():
    question = "Which of the following food choices do you prefer?\nA. Spaghetti\nB. Bratwurst\nC. Lomein\nD. Barbecued Meat\n>>> "

    food_preference = (raw_input(question)).upper()

    return food_preference

def within_Italy(preference):
    if preference == "A":
        print "You are on your way to Lombardy!"
    elif preference == "B":
        print "You are on your way to Emilia-Romagna!"
    elif preference == "C":
        print "You are on your way to Lazio!"
    elif preference == "D":
        print "You are on your way to Campania!"
    else:
        print "Choose from the choices on the menu."
        specify_region("Italy")

def within_Germany(preference):
    if preference == "A":
        print "You are on your way to Southwestern Germany!"
    elif preference == "B":
        print "You are on your way to Bavaria and Franconia!"
    elif preference == "C":
        print "You are on your way to the Rhineland!"
    elif preference == "D":
        print "You are on your way to Northeastern Germany!"
    else:
        print "Choose from the choices on the menu."
        specify_region("Germany")

def within_China(preference):
    if preference == "A":
        print "You are on your way to Guangdong Province!"
    elif preference == "B":
        print "You are on your way to Sichuan Province!"
    elif preference == "C":
        print "You are on your way to Jiangsu Province!"
    elif preference == "D":
        print "You are on your way to Hunan Province!"
    
    else:
        print "Choose from the choices on the menu."
        specify_region("China")

def within_Brazil(preference):
    if preference == "A":
        print "You are on your way to North Brazil!"
    elif preference == "B":
        print "You are on your way to Northeast Brazil!"
    elif preference == "C":
        print "You are on your way to Central-West Brazil!"
    elif preference == "D":
        print "You are on your way to Southeast Brazil!"
    else:
        print "Choose from the choices on the menu."
        specify_region("Brazil")

def specify_region(country):
    if country == "Italy":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Risotto\nB. Tortellini\nC. Spaghetti Alla Carbonara\nD. Calzone\n>>> "
        preference = (raw_input(further_preference)).upper()
        within_Italy(preference)
    elif country == "Germany":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Spatzle\nB. Knodel\nC. Potato Panckaes\nD. Currywurst\n>>> "
        preference = (raw_input(further_preference)).upper()
        within_Germany(preference)
    elif country == "China":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Dim Sum\nB. Sichuan Hotpot\nC. Sweet and Sour Mandarin Fish\nD. Spicy Chicken\n>>> "
        preference = (raw_input(further_preference)).upper()
        within_China(preference)
    elif country == "Brazil":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Acai Berry\nB. Bobo de Camarao (thick shrimp stew)\nC. Carne Seca com Banan Verde (sundried meat sauteed w onions, garlic, tomatoes, served w green bananas) \nD. Bolinhos de Bacalhao (fried croquettes made w dried cod)\n>>> "
        preference = (raw_input(further_preference)).upper()
        within_Brazil(preference)
    else:
        print "Please choose a country that is on our list. "

def ask_if_continue_to_region(country):
    next_question = (raw_input("Do you want to go to a specific region? ")).lower()

    if next_question == "yes":
        specify_region(country)
    elif next_question == "no":
        print "Ok."
    else:
        print "Please give a yes or no answer."

def creates_prints_destination(food_preference):

    if food_preference == "A":
        print "Let's go to Italy!"
        ask_if_continue_to_region("Italy")
    elif food_preference == "B":
        print "Let's go to Germany!"
        ask_if_continue_to_region("Germany")
    elif food_preference == "C":
        print "Let's go to China!"
        ask_if_continue_to_region("China")
    elif food_preference == "D":
        print "Let's go to Brazil!"
        ask_if_continue_to_region("Brazil")
    else:
        print "Please choose from among the food choices."
        ask_for_info()

def ask_if_repeat_whole_process():
    answer = (raw_input("Do you want to play again? ")).lower()
    if answer == "yes":
        True 
        return True
    elif answer == "no":
        False
        return False
    else:
        print "Give a yes or no answer."

        

greet_user()
playing = True
while playing:
    food_preference = ask_for_info()
    creates_prints_destination(food_preference)
    playing = ask_if_repeat_whole_process()