#Author: Langfish

MAX_INGREDIENTS = 100

#the main program
def main():
    ingredients = ["" for x in range(MAX_INGREDIENTS)]
    measurements = [0.0 for x in range(MAX_INGREDIENTS)]
    units = [0.0 for x in range(MAX_INGREDIENTS)]
    number_of_ingredients = 0
    welcome()
    number_of_ingredients = get_info(ingredients, measurements, units)
    recipe(number_of_ingredients,ingredients,measurements,units)

#error handling for getting a string
def get_string(prompt):
    value = ""

    value = input(prompt)
    return value

#error handling for entering y or n
def y_or_n(prompt):
    value = ""

    prompt = input(prompt)
    while True:
        if value == "Y" or value == "y":
            return True
        elif value == "N" or value == "n":
            return False
        else:
            print("Please enter Y or N!")
            value = input(prompt)

#error handling for getting a real number
def valid_real(value):
    try:
        float(value)
        return True
    except:
        return False

#error handling for inputing a number
def input_number(prompt):
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Not an integer! Try Again!")
            continue
        else:
            return userInput
            break

#gets a real number and makes sure it is valid through valid_real()
def get_real(prompt):
    value = ""

    value = input(prompt)
    while not valid_real(value):
        print(value, "is not a number. Try again!")
        value = input(prompt)
    return float(value)

#greets user with a welcome message
def welcome():
    print("Welcome to the Recipe Converter!")
    print(" ")
    print("I will assist you in figuring out what new measurements you need for your recipe with the amount of people that you are serving!")
    print("")

#gets all the information for the recipe
def get_info(ingredients, measurements, units):
    done = False
    counter = 0

    while not done:
        ingredients[counter] = get_string("What is the name of the ingredient? ")
        measurements[counter] = get_real("What is the measurement? ")
        units[counter] = units_list()
        counter += 1
        done = y_or_n("Are you done? (Y/N) ")
    return  counter

#displays the list of available units and allows selection
def units_list():
    units = ['Cups', 'Dashes', 'Ounces', 'Pinches', 'Tablespoons', 'Teaspoons', 'Pounds', 'Each', 'Cups', 'Drops',
             'Gallons', 'Ounces', 'Quarts']
    length = len(units)
    for i in range(length - 1):
        print(i, units[i])

    list_selection = int(input_number("Choose an option for the units from the list above! "))
    unit_selection = units[list_selection - 1]
    return unit_selection

#Converts to the new amount and displays the new recipe
def recipe(number_of_ingredients, ingredients, measurements, units):
    count = 0

    current_servings = int(input_number("How many people does the original recipe make? "))
    new_servings = input_number("How many people are you serving? ")
    conversion_factor = new_servings / current_servings

    print("The new recipe will be: ")

    while count < number_of_ingredients:
        print((measurements[count] * conversion_factor), units[count], ingredients[count])
        count = count + 1

main()
