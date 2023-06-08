from itertools import product

def get_user_details():
    name = input("Hi! How are you today? Please tell me your name: ")
    gender = input("Please enter your gender (M/F/D): ")
    print(f"\nHello {name} ({gender}), let's find the perfect outfit for you!\n")
    return name

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
            'headgear': [],
            'neckgear': [],
            't_shirt': ["half-sleeve T-shirt"],
            'sweaters': [],
            'jackets': [],
            'coats': [],
            'pants': ["cotton pants"],
            'socks': ["anklet"],
            'shoes': ["loafers", "sneakers"]
        },
        'Hot': {
            'headgear': ["neck covering hat"],
            'neckgear': [],
            't_shirt': ["v neckT-shirt"],
            'sweaters': [],
            'jackets': [],
            'coats': [],
            'pants': ["CHINOS"],
            'socks': ["anklet"],
            'shoes': ["sandals"]
        },
        'Pleasant': {
            'headgear': ["P cap"],
            'neckgear': [],
            't_shirt': ["sleeve T-shirt"],
            'sweaters': [],
            'jackets': ["Denim Jacket"],
            'coats': [],
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
            'coats': [],
            'pants': ["Jeans"],
            'socks': ["knee-high"],
            'shoes': ["Boots"]
        },
        'Freezing': {
            'headgear': ["Ski cap"],
            'neckgear': ["the Parisian scarf"],
            't_shirt': ["warmer half sleeve"],
            'sweaters': ["Cardigan"],
            'jackets': [],
            'coats': ["Dounen Mantel"],
            'pants': ["gefuttert jeans"],
            'socks': ["thigh-high"],
            'shoes': ["gefuttert boots"]
        },
        'Rainy': {
            'headgear': ["baseball cap"],
            'neckgear': [],
            't_shirt': ["half-sleeve T-shirt"],
            'sweaters': [],
            'jackets': [],
            'coats': ["TRENCH RAIN COAT"],
            'pants': ["CORDUROY"],
            'socks': ["mid-calf"],
            'shoes': ["gummistiefel"]
        }
    }

    print("Here are some clothing suggestions for you:")
    options = []
    for clothing_type, choices in clothing_options[weather].items():
        if choices:
            options.append(choices)
    for combination in product(*options):
        print(", ".join(combination))
    print("\nThank you for using Dress to Impress! You will kill it today.")

# Main program flow
name = get_user_details()
weather_choice = get_weather_choice()
give_clothing_suggestions(weather_choice)
if __name__ == "__main__":
    main()
