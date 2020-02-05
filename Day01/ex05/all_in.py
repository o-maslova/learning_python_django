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


def find_match(dictionary: dict, element: str):
    for key, value in dictionary.items():
        if value == element:
            return key
    return None


def make_output(lst: list):
    out = ""
    for elem in lst:
        # Normalization of a string (making first letter capital and other small)
        norm_elem = elem.title()

        # Search for a match in capital_cities list
        search_in_cities_res = find_match(capital_cities(), norm_elem)

        # Search for a match in states list
        search_in_states_res = states().get(norm_elem)

        if search_in_cities_res:
            out += "{city} is the capital of {state}\n".format(city=norm_elem,
                                                               state=find_match(states(), search_in_cities_res))
        elif search_in_states_res:
            out += "{city} is the capital of {state}\n".format(city=capital_cities().get(search_in_states_res),
                                                               state=norm_elem)
        else:
            if norm_elem != '':
                out += "{city} is neither a capital city nor a state\n".format(city=elem)
    return out[:-1]


def get_data(user_input: str):
    list_of_states = user_input.split(',')
    list_of_states = [elem.strip() for elem in list_of_states]
    return make_output(list_of_states)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].strip() != "":
        print(get_data(sys.argv[1]))
