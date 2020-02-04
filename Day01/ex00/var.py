def my_var():
    num = 42
    string = "42"
    num_to_string = "forty two"
    float_num = 42.0
    boolean = True
    lst = [42]
    dictionary = {42: 42}
    tup = (42,)
    my_set = set()

    out = [num,  string, num_to_string, float_num, boolean, lst, dictionary, tup, my_set]
    for elem in out:
        print("{what} has the type {var_type}".format(what=elem, var_type=type(elem)))


if __name__ == '__main__':
    my_var()
