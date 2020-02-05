import sys


def states():
    return {
        "Oregon"    : "OR",
        "Alabama"   : "AL",
        "New Jersey": "NJ",
        "Colorado"  : "CO"
    }


def capital_cities():
    return {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }


def find_match(user_input: str):
    match = states().get(user_input)
    if not match:
        return "Unknown state"
    else:
        return capital_cities().get(match)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(find_match(sys.argv[1]))
