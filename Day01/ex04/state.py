import sys

states = {
    "Oregon"    : "OR",
    "Alabama"   : "AL",
    "New Jersey": "NJ",
    "Colorado"  : "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}


def find_state(state):
    for key, value in states.items():
        if value == state:
            return key


def find_match(user_input: str):
    for key, value in capital_cities.items():
        if user_input == value:
            return find_state(key)
    return "Unknown capital city"


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(find_match(sys.argv[1]))
