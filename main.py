def get_user_details():
    name = input("Hi! How are you today? Please tell me your name: ")
    gender = input("Please enter your gender (M/F/D): ")
    if gender == 'M':
        gender_text = "Mr."
    elif gender == 'F':
        gender_text = "Ms."
    else:
        gender_text = "Mx."
    print(f"\nHello {gender_text} {name}! Let us dress you to impress today")

def get_weather_choice():
    print("Please choose the type of weather from the following options:")
    print("a. Warm")
    print("b. Hot")
    print("c. Pleasant")
    print("d. Cold")
    print("e. Freezing")
    print("f. Rainy")

    weather_options = {
        'a': 'Warm',
        'b': 'Hot',
        'c': 'Pleasant',
        'd': 'Cold',
        'e': 'Freezing',
        'f': 'Rainy'
    }
    selected_weather = input("Enter the option letter: ")
    print(f"\nSelected weather: {weather_options[selected_weather]}\n")
    return weather_options[selected_weather]

def give_clothing_suggestions(weather):
    clothing_options = {
        'Warm': {
            't_shirt': ["half-sleeve T-shirt"],
            'pants': ["cotton pants"],
            'socks': ["anklet"],
            'shoes': ["loafers", "sneakers"]
        },
        'Hot': {
            'headgear': ["neck covering hat"],
            't_shirt': ["v neck T-shirt"],
            'pants': ["CHINOS"],
            'socks': ["anklet"],
            'shoes': ["sandals"]
        },
        'Pleasant': {
            'headgear': ["P cap"],
            't_shirt': ["sleeve T-shirt"],
            'jackets': ["Denim Jacket"],
            'pants': ["LINEN"],
            'socks': ["half socks"],
            'shoes': ["sneakers"]
        },
        'Cold': {
            'headgear': ["beanie"],
            'neckgear': ["reverse drape scarf"],
            't_shirt': ["turtle-neck T-shirt"],
            'sweaters': ["Quarter-Zip", "Vest"],
            'jackets': ["Trucker Jacket"],
            'pants': ["Jeans"],
            'socks': ["knee-high"],
            'shoes': ["Boots"]
        },
        'Freezing': {
            'headgear': ["Ski cap"],
            'neckgear': ["the Parisian scarf"],
            't_shirt': ["warmer half sleeve"],
            'sweaters': ["Cardigan"],
            'coats': ["Dounen Mantel"],
            'pants': ["gefuttert jeans"],
            'socks': ["thigh-high"],
            'shoes': ["gefuttert boots"]
        },
        'Rainy': {
            'headgear': ["baseball cap"],
            't_shirt': ["half-sleeve T-shirt"],
            'coats': ["TRENCH RAIN COAT"],
            'pants': ["CORDUROY"],
            'socks': ["mid-calf"],
            'shoes': ["gummistiefel"]
        }
    }

    print("Here are some clothing suggestions for you:")
    options = clothing_options.get(weather, {})
    for clothing_type, choices in options.items():
        if choices:
            print(f"{clothing_type.capitalize()}: {', '.join(choices)}")
    print("\nThank you for using Dress to Impress! You will kill it today.")

name = get_user_details()
weather_choice = get_weather_choice()
give_clothing_suggestions(weather_choice)
