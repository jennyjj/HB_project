import re 

def greet_user():
    print "Welcome to Where Will Your Tastes Lead You?"
    print "We look forward to seeing where you will go!"

def create_foods(my_trip, food):
    my_trip["foods"].append(food)

def ask_for_info():
    question = "Which of the following food choices do you prefer?\nA. Spaghetti\nB. Bratwurst\nC. Lomein\nD. Barbecued Meat\n>>> "
    
    food_preference = (raw_input(question)).upper()

    if food_preference == "A":
        food = "Spaghetti"
    elif food_preference == "B":
        food = "Bratwurst"
    elif food_preference == "C":
        food = "Lomein"
    elif food_preference == "D":
        food = "Barbecued Meat"

    create_foods(my_trip, food)

    return food_preference
    
def create_region_locations(my_list, key, region):
    my_trip[key].append(region)

def within_Italy(preference):
    if preference == "A":
        print "You are on your way to Lombardy!"
        region = "Lombardy"
    elif preference == "B":
        print "You are on your way to Emilia-Romagna!"
        region = "Emilia-Romagna"
    elif preference == "C":
        print "You are on your way to Lazio!"
        region = "Lazio"
    elif preference == "D":
        print "You are on your way to Campania!"
        regino = "Campania"
    else:
        print "Choose from the choices on the menu."
        specify_region("Italy")

    create_region_locations(my_trip, "regions", region)

def within_Germany(preference):
    if preference == "A":
        print "You are on your way to Southwestern Germany!"
        region = "Southwestern Germany"
    elif preference == "B":
        print "You are on your way to Bavaria and Franconia!"
        region = "Bavaria and Franconia"
    elif preference == "C":
        print "You are on your way to the Rhineland!"
        region = "Rhineland"
    elif preference == "D":
        print "You are on your way to Northeastern Germany!"
        region = "Northeastern Germany"
    else:
        print "Choose from the choices on the menu."
        specify_region("Germany")

    create_region_locations(my_trip, "regions", region)

def within_China(preference):
    if preference == "A":
        print "You are on your way to Guangdong Province!"
        region = "Guangdong Province"
    elif preference == "B":
        print "You are on your way to Sichuan Province!"
        region = "Sichuan Province"
    elif preference == "C":
        print "You are on your way to Jiangsu Province!"
        region = "Jiangsu Province"
    elif preference == "D":
        print "You are on your way to Hunan Province!"
        region = "Hunan Province"
    else:
        print "Choose from the choices on the menu."
        specify_region("China")

    create_region_locations(my_trip, "regions", region)

def within_Brazil(preference):
    if preference == "A":
        print "You are on your way to North Brazil!"
        region = "North Brazil"
    elif preference == "B":
        print "You are on your way to Northeast Brazil!"
        region = "Northeast Brazil"
    elif preference == "C":
        print "You are on your way to Central-West Brazil!"
        region = "Central-West within_Brazil"
    elif preference == "D":
        print "You are on your way to Southeast Brazil!"
        region = "Southeast Brazil"
    else:
        print "Choose from the choices on the menu."
        specify_region("Brazil")

    create_region_locations(my_trip, "regions", region)

def specify_region(country):
    if country == "Italy":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Risotto\nB. Tortellini\nC. Spaghetti Alla Carbonara\nD. Calzone\n>>> "
        preference = (raw_input(further_preference)).upper()

        if preference == "A":
            food = "Risotto"
        elif preference == "B":
            food = "Tortellini"
        elif preference == "C":
            food = "Spaghetti Alla Carbonara"
        elif preference == "D":
            food = "Calzone"
        create_foods(my_trip, food)
        
        within_Italy(preference)                   

    elif country == "Germany":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Spatzle\nB. Knodel\nC. Potato Panckaes\nD. Currywurst\n>>> "
        preference = (raw_input(further_preference)).upper()

        if preference == "A":
            food = "Spatzle"
        elif preference == "B":
            food = "Knodel"
        elif preference == "C":
            food = "Potato Pancakes"
        elif preference == "D":
            food = "Currywurst"
        create_foods(my_trip, food)

        within_Germany(preference)

    elif country == "China":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Dim Sum\nB. Sichuan Hotpot\nC. Sweet and Sour Mandarin Fish\nD. Spicy Chicken\n>>> "
        preference = (raw_input(further_preference)).upper()

        if preference == "A":
            food = "Dim Sum"
        elif preference == "B":
            food = "Sichuan Hotpot"
        elif preference == "C":
            food = "Sweet and Sour Mandarin Fish"
        elif preference == "D":
            food = "Spicy Chicken"
        create_foods(my_trip, food)

        within_China(preference)

    elif country == "Brazil":
        further_preference = "Which of these sounds the most appetizing to you?\nA. Acai Berry\nB. Bobo de Camarao (thick shrimp stew)\nC. Carne Seca com Banan Verde (sundried meat sauteed w onions, garlic, tomatoes, served w green bananas) \nD. Bolinhos de Bacalhao (fried croquettes made w dried cod)\n>>> "
        preference = (raw_input(further_preference)).upper()
        
        if preference == "A":
            food = "Acai Berry"
        elif preference == "B":
            food = "Bobo de Camarao"
        elif preference == "C":
            food = "Carne Seca com Banan Verde"
        elif preference == "D":
            food = "Bolinhos de Bacalhao"
        create_foods(my_trip, food)

        within_Brazil(preference)

def create_country_locations(my_trip, key, country):
    my_trip[key].append(country)

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
        country = "Italy"
    elif food_preference == "B":
        print "Let's go to Germany!"
        country = "Germany"
    elif food_preference == "C":
        print "Let's go to China!"
        country = "China"
    elif food_preference == "D":
        print "Let's go to Brazil!"
        country = "Brazil"

    create_country_locations(my_trip, "countries", country)
    ask_if_continue_to_region(country)

def _format_list_to_string(list_to_convert_to_string):
    list_to_convert_to_string.insert(-1, ' and')
    new_string = ','.join(list_to_convert_to_string)
    print new_string
    return new_string

def create_a_map(my_trip):
    formatted_string_countries = _format_list_to_string(my_trip["countries"])
    if my_trip["regions"] == []:   
        print "You have traveled to the country/ies of {}.".format(formatted_string_countries)
    else:
        formatted_string_regions = _format_list_to_string(my_trip["regions"])
        print "You have traveled to the region(s) of {} in the country/ies of {}.".format(formatted_string_regions, formatted_string_countries) 

def create_menu(my_trip):   
    formatted_string_foods = _format_list_to_string(my_trip["foods"])
    print "You have enjoyed tasting {}.".format(formatted_string_foods)

def ask_if_repeat_whole_process():
    answer = (raw_input("Do you want to play again? ")).lower()
    if answer == "yes":
        return True
    if answer == "no":
        return False
    else:
        return 2


my_trip = {"countries": [], "regions": [], "foods": []}
playing = True
while playing:
    if playing == 2:
        print "Please enter 'yes' or 'no'"
        playing = ask_if_repeat_whole_process()
        continue
    food_preference = ask_for_info()
    creates_prints_destination(food_preference)
    create_a_map(my_trip)
    create_menu(my_trip)
    playing = ask_if_repeat_whole_process()
print "Thanks for playing my game!"